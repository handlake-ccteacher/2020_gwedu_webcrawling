import requests
import json
import os

class NaverImage:
    def __init__(self, nid = 'IYqDoDwczfqSVZ8zC4pA', npass='4SASN4JMXn'):
        self.naverID = nid
        self.naverSecret = npass
        self.query = 'AI'
        self.display = 100
        self.start = 1
        self.sort = 'sim'
        self.filter = 'large'
        self.makeURL()

    def makeURL(self):
        baseurl = 'https://openapi.naver.com/v1/search/image'
        self.url = baseurl + f'?query={self.query}'
        self.url += f'&display={self.display}'
        self.url += f'&start={self.start}'
        self.url += f'&sort={self.sort}'
        self.url += f'&filter={self.filter}'
    
    def get(self):
        headers = {'X-Naver-Client-Id':self.naverID, 'X-Naver-Client-Secret':self.naverSecret}
        rtn = requests.get(self.url, headers=headers)
        if rtn.ok:
            return rtn
        return None

    def getjson(self):
        return self.get().json()

    def getImageURLs(self):
        jData = self.getjson()
        rlist = []
        for img in jData['items']:
            rlist.append(img['link'])
        return rlist

    def myNaver(self):
        print(f'NAVER ID : {self.naverID}, NAVER SECRET : {self.naverSecret}')
        print(f'URL : {self.url}')


    def setQuery(self, query):
        self.query = query
        self.makeURL()


    def setDisplay(self, display):
        self.display = display
        self.makeURL()

    def setStart(self, start):
        self.start = (start-1)*self.display+1
        self.makeURL()

    def setSort(self, sort):
        if type(sort) is str:
            if s.strip() == 'date':
                self.sort = 'date'
            else:
                self.sort = 'sim'
        elif type(sort) is int:
            if s==0:
                self.sort = 'sim'
            else:
                self.sort = 'date'
        else:
            self.sort = 'sim'
        self.makeURL()

    def setFilter(self, filter):
        self.filter = filter
        self.makeURL()

    def getImage(self):
        imgurls = self.getImageURLs()
        tmpFolder = self.query
        tmpadd = 0
        while os.path.exists(tmpFolder):
            tmpadd += 1
            tmpFolder = self.query+str(tmpadd)
        os.mkdir(tmpFolder)
        os.chdir(tmpFolder)
        imgnum = 0
        for imgurl in imgurls:
            res_image = requests.get(imgurl)
            if res_image.ok:
                imgnum+=1
                with open(f'{self.query}{imgnum}.jpg', 'wb') as f:
                    f.write(res_image.content)
        
        os.chdir('..')       




if __name__=='__main__':
    n = NaverImage()
    search = input('검색어 입력 : ')
    n.setQuery(search)
    for i in range(10):
        n.setStart(i+1)
        n.getImage()