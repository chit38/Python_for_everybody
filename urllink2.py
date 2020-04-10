# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('td')
final = list()
for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print(tag.get('herf', None))
    temp = str(tag.contents[0])
    Contents= re.findall('[0-9]+', temp)
    if len(Contents)>0:
        for content in Contents:
            content= int(content)
            final.append(content)
    #print('Attrs:', tag.attrs)
print(sum(final))