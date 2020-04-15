import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
tags = soup('p')
for tag in tags:
    link=tag.get('href', None)
    if link is not None:
        if link.startswith("http"):
            print(link)
        
        


