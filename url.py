from lxml import html
import requests
import re
import os
import xml.etree.ElementTree as ET
from mutagen.id3 import ID3
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


def get_filename(cd):
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]


def save_defined_file(filename, year, r):
    open(filename, 'wb').write(r.content)
    audio = ID3(filename)
    print(audio["TDRC"], filename, "\n")
    if(int(str(audio["TDRC"])) <= year):
        print("hello there")
        os.remove(filename)
        return False
    return True


def download_mp3(link, year):
    if link.endswith('.mp3') or link.endswith('.m4a'):
        r = requests.get(link, allow_redirects=True)
        filename = get_filename(r.headers.get('content-disposition'))
        if filename is None:
            filename = link.rsplit('/', 1)[1]
        if save_defined_file(filename, year, r):
            return filename
        return None
    return None


def get_urls(url, i, year):
    page = requests.get(url)
    webpage = html.fromstring(page.content)
    flag = False
    for link in webpage.xpath('//a/@href'):
        if i > 1:
            if re.match(r"https?:\/\/.*", link):
                get_urls(link, i-1)
            else:
                parsed_uri = urlparse(url[:len(url)-1])
                domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
                get_urls(domain+link, i-1)
        else:
            download_mp3(link, year)
            flag = True
    return flag


tree = ET.parse('url.xml')
root = tree.getroot()
depth = int(root.find('depth').text)
year = int(root.find('year').text)
for url in tree.find('urls').findall('url'):
    get_urls(url.text.strip(), depth, year)
