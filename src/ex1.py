#!/usr/bin/env python
import urllib2
from bs4 import BeautifulSoup, SoupStrainer

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

# print all links in the page
# TODO: convert relative url to absolute
def print_all_links(page):

    soup = BeautifulSoup(page, "lxml", parse_only=SoupStrainer('a', href=True))

    for link in soup.find_all("a", href=True):
        print (link['href'])


print_all_links(get_page('http://randomwits.com'))

