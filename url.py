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
        return False
    return False


def get_urls(url, i, year):
    page = requests.get(url)
    webpage = html.fromstring(page.content)
    found = False
    for link in webpage.xpath('//a/@href'):
        if download_mp3(link, year):
            found = True
        if i > 1:
            if re.match(r"https?:\/\/.*", link):
                get_urls(link, i-1, year)
            else:
                parsed_uri = urlparse(url[:len(url)-1])
                domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
                print(link)
                get_urls(domain[:len(domain)-1]+link, i-1, year)
    return found


tree = ET.parse('url.xml')
root = tree.getroot()
depth = int(root.find('depth').text)
year = int(root.find('year').text)
for url in tree.find('urls').findall('url'):
    get_urls(url.text.strip(), depth, year)
