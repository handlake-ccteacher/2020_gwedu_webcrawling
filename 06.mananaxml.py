import requests
from xml.etree import ElementTree

xmlurl = 'https://api.manana.kr/exchange/rate/KRW/KRW,USD,JPY.xml'
xmlresp = requests.get(xmlurl)
if xmlresp.ok :
    print(xmlresp.text)
root = ElementTree.fromstring(xmlresp.content)
items = root.findall('item')
print(type(root))
for item in items:
    for data in item:
        if data.tag=='name' and 'USD' in data.text:
            print(item[2].text)

''''
print(len(items))
for e in items.pop().getchildren():
    print(f'{e.tag} : {e.text}')
    '''