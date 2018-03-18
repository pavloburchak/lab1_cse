from lxml import html
import requests
import re
import xml.etree.ElementTree as ET
from urllib.parse import urlparse

def download_mp3(link)
    if link.endswith('.mp3')
        r = requests.get(link, allow_redirects=True)
        open(link + '.mp3', 'wb').write(r.content)
        

def get_urls(url, i):
    page = requests.get(url)
    webpage = html.fromstring(page.content)
    for link in webpage.xpath('//a/@href'):
        if i > 1:
            if re.match(r"https?:\/\/.*", link):
                get_urls(link, i-1)
            else:
                parsed_uri = urlparse( url[:len(url)-1] )
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