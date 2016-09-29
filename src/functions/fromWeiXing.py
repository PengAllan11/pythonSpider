#coding=utf-8
#__author__ = "peng_an"

import urllib
import urllib2
import re
from bs4 import BeautifulSoup
import types


page = 1
url = 'http://weixin.sogou.com/weixin'
values ={'query': '中欧班列', 'type': '2', 'ie': 'utf8', 'page': page}

encoded_param = urllib.urlencode(values)
full_url = url + '?' + encoded_param
print full_url

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
try:
    request = urllib2.Request(full_url, headers=headers)
    response = urllib2.urlopen(request)
    content = response.read()
    #解析的一种方法
    # pattern = re.compile('<a href.*?target="_blank" id="sogou_vr.*?>(.*?)</a>',re.S)
    # items = re.findall(pattern,content)
    # for item in items:
    #     print item

    #用bs4解析
    soup = BeautifulSoup(content, "lxml")


except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

# 删除所有的无效字符，比如空格，引号，换行符等
def formatstr(dealStr):
    if(type(dealStr) is not types.StringType):
        dealStr = dealStr.encode('utf-8')
    dealStr = "".join(dealStr.split())
    #print dealStr
    dealStr = dealStr.replace('"', '')
    #print dealStr
    dealStr = dealStr.replace("​", "")
    return dealStr


# 处理获取的网页
allTitles = soup.find_all('div', class_=re.compile("txt-box"))
for item in allTitles:
    title = item.find('a', id=re.compile("sogou_vr_11002601_title_\d"))
    titleHref = title['href'].encode('utf-8')
    titleName = title.get_text().encode('utf-8')
    print titleName
    print titleHref

#
#
# # file_object = open('weixing.txt', 'w')
# # try:
# #     file_object.write(titleName+"\n")
# #     file_object.write(titleHref)
# # finally:
# #     file_object.close()
