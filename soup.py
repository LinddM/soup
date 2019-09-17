#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys,csv,json

import pages.portal as portal
import pages.estudios as estudios
import pages.cs as cs
import pages.directorio as directorio

url="http://ufm.edu/Portal"
# Make a GET request to fetch the raw HTML content
try:
    html_content = requests.get(url).text
except:
    print(f"unable to get {url}")
    sys.exit(1)

# Parse the html content, this is the Magic ;)
soup = BeautifulSoup(html_content, "html.parser")

## print entire html
# print(soup.prettify())

## print title (with tags)
# print(soup.title)
## # print title (without tags)
# print(soup.title.string)

'''
for div in soup.find_all("div"):
    print(div)
    print("--------------------------")
'''

separator_parts = '============================='
separator_items = '------------------------------------------'

if __name__ == "__main__":
    print('Lindsey\n')
    print(portal.output)