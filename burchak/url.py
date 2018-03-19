from lxml import html
import requests
import re
import xml.etree.ElementTree as ET
from urllib.parse import urlparse
from mutagen.id3 import ID3


def get_filename(cd):
    print(cd)
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]


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
            if link.endswith('.mp3'):
                r = requests.get(link, allow_redirects=True)
                filename = "BB.mp3"
#                filename = get_filename(r.headers.get('content-disposition'))
                print(link, filename, "\n")
                if filename is not None:
                    print("aa")
                    open(filename, 'wb').write(r.content)
                    audio = ID3(filename)
                    print(audio)
#                    print(ID3.getall('TIT2'))
    return


tree = ET.parse('url.xml')
root = tree.getroot()
depth = int(root.find('depth').text)
for url in tree.find('urls').findall('url'):
    get_urls(url.text.strip(), depth)
