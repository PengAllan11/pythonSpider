# encoding: utf-8
"""
@author: peng_an
@time: 2016/5/6 20:38
"""
import urllib
import urllib2
from bs4 import BeautifulSoup
import json

class indexSearch:

    def __init__(self, query, url='http://index.so.com/#trend'):
        self.url = url
        self.query = query
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        values = {'query': query, 'type': '2', 'ie': 'utf8', 'page': 1}
        # get complete url of a key word
        self.url = self.url + '?' + urllib.urlencode(values)
        self.soup = None
        self.index_url = None
        #print self.url

    def get_search_index(self, query, url):
        self.index_url = url
        values = {'a':'soIndexJson','area':'全国','q':query}
        self.index_url = self.index_url + '?' + urllib.urlencode(values)
        data = urllib.urlopen(self.index_url)
        searchinfo = json.loads(data.read())

        print self.index_url
        print json.dumps(searchinfo['data']['index'].keys(), ensure_ascii=False)

        try:
            for ikey in searchinfo['data']['index'].keys():
                data = searchinfo['data']['index'][ikey]
                data.replace('u', '')
                data = data.replace('\"', '')
                data = data.split('|')
                print data
            lastTime = searchinfo['data']['period']['to']
            print lastTime
        except Exception as e:
            print e



if __name__ == '__main__':
    search_360 = indexSearch('渝新欧,中欧班列')
    search_360.get_search_index('渝新欧,中欧班列','http://index.so.com/index.php')