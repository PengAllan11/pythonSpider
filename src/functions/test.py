#coding=utf-8
#__author__ = "peng_an"

import re
from bs4 import BeautifulSoup
import os

#该文件包含一些简单的用法

#list中的String转int
#print map(int,["1","2","3","4"])

content = """
<div class="txt-box1"></div>
"""

#以字符串的形式输出json格式的数据
#print json.dumps(content, ensure_ascii=False)

soup = BeautifulSoup(content, "lxml")
div1 = soup.find('div', class_=re.compile("txt-box\d"))
print div1

print "sasa|assas|sas".split('|')

print "fdkanfa"[1:-4]

