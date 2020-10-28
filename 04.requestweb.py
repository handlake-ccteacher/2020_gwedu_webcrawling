import requests

url = 'http://www.google.com'
resp = requests.get(url)
print(resp.ok)
print(resp.text[:80])
print(dir(resp))
print(resp.reason)
print(resp.request)