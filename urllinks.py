# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
def func(url,rc):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    if rc==repeat:
        return print(url)
    posc=0
    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        posc=posc + 1
        if posc==pos:
            func(tag.get('href', None), rc+1)
            print(tag.get('href', None))
            break
        


url = input('Enter - ')
pos=18
repeat=7
func(url,0)

