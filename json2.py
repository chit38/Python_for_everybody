import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter link: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
#print(json.dumps(info, indent=2))
ans=list()
for item in info["comments"]:
    temp=int(item["count"])
    ans.append(temp)
print(sum(ans))