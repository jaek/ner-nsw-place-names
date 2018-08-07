#!/bin/python

from bs4 import BeautifulSoup as bs
import urllib.request
from subprocess import call

response = urllib.request.urlopen('http://gutenberg.net.au/plusfifty-a-m.html')
html = response.read()
soup = bs(html)
prefix = "http://gutenberg.net.au/"

for link in soup.findAll('a', href=True, text='Text'):
    call(["wget",  prefix + link['href']])
