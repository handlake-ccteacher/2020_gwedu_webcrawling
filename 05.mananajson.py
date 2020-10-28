import requests

reurl = 'https://api.manana.kr/exchange.json'
# https://api.manana.kr/exchange/rate/KRW/KRW,USD,JPY.json'
# https://api.manana.kr/exchange/rate.json?base=KRW&code=KRW,USD,JPY
# 국가코드 symbol로 알아보면됨...


jresp = requests.get(reurl)
jdata = jresp.json()
print(type(jdata))
print(len(jdata))
print(jdata[0])
print(type(jdata[0]))
for i in range(5):
    for key, value in jdata[i].items():
        print(key,':',value)

na = input('국가 : ')
for data in jdata:
    for k, v in data.items():
        if k=='kr' and na in v:
            print(data['kr'], ':', data['price'])
