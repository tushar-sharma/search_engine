#!/usr/bin/env python
import urllib2

# get page get the source code and return string
def get_page(page):
    response = urllib2.urlopen(page)
    page_source = response.read()

    return page_source
