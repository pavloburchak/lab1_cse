from lxml import html
import requests
import re

def get_urls(url, i):
    page = requests.get(url)
    webpage = html.fromstring(page.content)
    for link in webpage.xpath('//a/@href'):
        if i > 1:
            if re.match(r'https?:\/\/.*',link):
                get_urls(link, i-1)
            else:
                get_urls(url[:len(url)-1]+link,i-1)
        else:
            print(link,"url",url,"\n")
    return;

get_urls('http://gdk-kpi.herokuapp.com/',2)
