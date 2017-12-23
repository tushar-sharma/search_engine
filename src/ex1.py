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

# extract href in html
def get_next_target(page):
    start_link = page.find('<a href=')

    if start_link == -1:
        return None, 0

    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)

    url = page[start_quote + 1:end_quote]
    return url, end_quote

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

