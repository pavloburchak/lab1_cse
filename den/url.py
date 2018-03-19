from lxml import html
import requests
import re
import xml.etree.ElementTree as ET
from urllib.parse import urlparse


def save_defined_file(filename, year):
    if(filename is not None):
        open(filename, 'wb').write(r.content)
        audio = ID3(filename)
        if(audio["TDRC"] <= year):
            os.remove(filename)


def get_filename_from_cd(cd):
    """
    Get filename from content-disposition
    """
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]


def download_mp3(link):
    if link.endswith('.mp3'):
        r = requests.get(link, allow_redirects=True)
        filename = get_filename_from_cd(r.headers.get('content-disposition'))
        save_defined_file(filename, 2015)


def get_urls(url, i):
    page = requests.get(url)
    webpage = html.fromstring(page.content)
    for link in webpage.xpath('//a/@href'):
        if i > 1:
            if re.match(r"https?:\/\/.*", link):
                get_urls(link, i-1)
            else:
                parsed_uri = urlparse(url[:len(url)-1])
                domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
                get_urls(domain+link, i-1)
        else:
            download_mp3(link)
    return


tree = ET.parse('ulr.xml')
root = tree.getroot()
depth = int(root.find('depth').text)
print(depth)
for url in tree.find('urls').findall('url'):
    get_urls(url.text.strip(), depth)
