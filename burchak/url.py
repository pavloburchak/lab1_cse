from lxml import html
import requests
import re
import xml.etree.ElementTree as ET
from urllib.parse import urlparse

parsed_uri = urlparse( 'http://stackoverflow.com/questions/1234567/blah-blah-blah-blah' )
domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
print (domain)

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
            print(link, "url", url, "\n")
    return


tree = ET.parse('ulr.xml')
root = tree.getroot()
depth = int(root.find('depth').text)
print(depth)
for url in tree.find('urls').findall('url'):
    get_urls(url.text.strip(), depth)
