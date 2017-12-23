#!/usr/bin/env python
import urllib2
from bs4 import BeautifulSoup, SoupStrainer
from urlparse import urljoin  
from urlparse import urlparse 

seed_page = "http://randomwits.com"

# get page get the source code and return string
def get_page(page):
    response = urllib2.urlopen(page)
    page_source = response.read()

    return page_source

# check if relative url or absolute
def is_absolute(link):
    return bool(urlparse(link).netloc)

# convert relative to absolute url
def to_absolute(url, link):
    return urljoin(url, link)

# print all links in the page
# TODO : remove mail to links
def print_all_links(page, seed_page):

    soup = BeautifulSoup(page, "lxml", parse_only=SoupStrainer('a', href=True))

    for link in soup.find_all("a", href=True):
        if not is_absolute(link['href']):
            print (to_absolute(seed_page, link['href']))
        else:
            print (link['href'])

print_all_links(get_page(seed_page), seed_page)

