from bs4 import BeautifulSoup as bs
import requests

xmlurl = 'https://api.manana.kr/exchange/rate/KRW/KRW,USD,JPY.xml'
xmlresp = requests.get(xmlurl)
if xmlresp.ok:
    soup = bs(xmlresp.content, 'html.parser')
print(type(soup))
print(soup.prettify())
items = soup.find_all('item')
print(type(items))
for item in items:
    print(item.name)
    print(item.text)
