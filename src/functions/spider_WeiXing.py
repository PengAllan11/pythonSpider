# encoding: utf-8
"""
@author: peng_an
@time: 2016/4/24 20:04
"""

import urllib
import urllib2
import re
from bs4 import BeautifulSoup
import types
import os
import shutil

class KeyArticles :

    def __init__(self, query, url='http://weixin.sogou.com/weixin'):
        self.url = url
        self.query = query
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        values = {'query': query, 'type': '2', 'ie': 'utf8', 'page': 1}
        # get complete url of a key word
        self.url = self.url + '?' + urllib.urlencode(values)
        self.soup = None
        self.index_name = None
        print self.url

    def get_indexes(self):
        # create a folder
        print os.getcwd()
        index = self.query.decode('utf-8')

        # delete the folder and its all files
        if os.path.isdir(index):
            shutil.rmtree(index)
        os.mkdir(index)

        # get the page data and transfer it to bs4 format
        try:
            request = urllib2.Request(self.url, headers=self.headers)
            response = urllib2.urlopen(request)
            content = response.read()
            self.soup = BeautifulSoup(content, "lxml")

        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason

    @staticmethod
    def format_str(deal_str):
        if type(deal_str) is not isinstance(types.StringType):
            deal_str = deal_str.encode('utf-8')
        deal_str = "".join(deal_str.split())
        # print dealStr
        deal_str = deal_str.replace('"', '')
        # print dealStr
        deal_str = deal_str.replace("​", "")
        return deal_str

    @staticmethod
    def format_title(title):
        title = title.decode('utf-8').strip()
        title = title.replace(':', '')
        title = title.replace('"', '')
        title = title.replace('\\', '')
        title = title.replace('?', '')
        title = title.replace('\/', '')
        title = title.replace('*', '')
        title = title.replace('<', '')
        title = title.replace('>', '')
        title = title.replace('|', '')
        return title

    def process_save(self):
        if self.soup is None:
            print "No data"
            return
        try:
            file_name = 'index----' + self.query+ '.txt'
            self.index_name = file_name.decode('utf-8')
            file_key = open(self.query.decode('utf-8') + '/' + file_name.decode('utf-8'), 'w')

            all_titles = self.soup.find_all('div', class_=re.compile("txt-box"))
            for item in all_titles:
                title = item.find('a', id=re.compile("sogou_vr_11002601_title_\d"))
                title_href = title['href'].encode('utf-8')
                title_name = title.get_text().encode('utf-8')
                # print title_name
                # print title_href
                file_key.write(title_name + "\n")
                file_key.write(title_href + "\n\n")
        except IOError as err:
            print err
        finally:
            file_key.close()

    def get_article_from_indexes(self):
        try:
            index_context = open(self.query.decode('utf-8') + '/' + self.index_name, 'r')

            while True:
                title = index_context.readline()
                if title and title != "\n" and title != "":
                    a = index_context.readline()
                    # self.get_article_from_url(a)
                    index_context.readline()
                    title = self.format_title(title)
                    article = open(self.query.decode('utf-8') + '/' + title+'.txt', 'w')
                    article.write(self.get_article_from_url(a).encode('utf-8'))
                    article.close()
                else:
                    break
        except IOError as err:
            print err
        finally:
            index_context.close()

    def get_article_from_url(self, url):
        print url
        request = urllib2.Request(url, headers=self.headers)
        response = urllib2.urlopen(request)
        content = response.read()
        soup = BeautifulSoup(content, "lxml")

        context = soup.find('div', class_="rich_media_content")
        return context.get_text()


if __name__ == '__main__':
    china_europe = KeyArticles('中欧班列')
    china_europe.get_indexes()
    china_europe.process_save()
    china_europe.get_article_from_indexes()

