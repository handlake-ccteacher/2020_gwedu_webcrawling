import os
import requests
import json

class NImage:
    def __init__(self, nid='IYqDoDwczfqSVZ8zC4pA', nsecret='4SASN4JMXn'):
        self.nid = nid
        self.nsec = nsecret
        self.query = 'AI'
        self.display = 100
        self.start = 1
        self.sort = 'sim'
        self.filter = 'large'
        self.requrl = ''
        self.makeUrl()
    
    def makeUrl(self):
        baseurl = 'https://openapi.naver.com/v1/search/image'
        self.requrl = baseurl + '?query='+self.query
        self.requrl += '&display='+str(self.display)
        self.requrl += '&start='+str(self.start)
        self.requrl += '&sort='+self.sort
        self.requrl += '&filter='+self.filter

    def __str__(self):
        return self.requrl

    def setQuery(self, query):
        self.query = query
        self.makeUrl()

    def get(self):
        q = input('찾을 이미지 : ')
        td = q
        tp = 0
        while os.path.exists(td):
            td = td+str(tp)
            tp+=1
        os.mkdir(td)
        os.chdir(td)

        self.setQuery(q)
        print(self.requrl)
        reqheaders = {'X-Naver-Client-Id':self.nid, 'X-Naver-Client-Secret':self.nsec}
        niresp = requests.get(self.requrl, headers=reqheaders)
        #print(niresp.ok)
        if niresp.ok:
            jdata = json.loads(niresp.content)
            items = jdata['items']
           # print(type(items))
           # print(type(items[0]))
            n=0
            for item in items:
                imgurl = item['link']
                ext = imgurl[imgurl.rfind('.'):]
                img = requests.get(imgurl)
                if img.ok:
                    with open(f'{self.query}{n}.jpg', 'bw') as f:
                        f.write(img.content)
                        n+=1
                        print('.',end='')
            print()          
if __name__=='__main__':
    n = NImage()
    n.get()