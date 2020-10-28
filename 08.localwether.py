import requests
from bs4 import BeautifulSoup

local = input('지역 : ')
weurl = f'https://search.naver.com/search.naver?query={local}날씨'
weresp = requests.get(weurl)
soup = BeautifulSoup(weresp.content.decode('utf-8'), 'html.parser')
wedata = soup.find('div', 'main_info')
print(wedata.prettify())
doc = wedata.find('span', 'todaytemp')
print(f'온도 : {doc.text} ')
dustdata = soup.find('div', 'sub_info')
print(dustdata.prettify())