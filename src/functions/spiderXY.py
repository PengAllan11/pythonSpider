# encoding: utf-8
"""
@author: peng_an
@time: 2016/7/11 20:06
"""

import urllib
import json

def geoGrabBaidu(location):
    apiStem = 'http://api.map.baidu.com/geocoder/v2/?'  #create a dict and constants for the goecoder
    params = {}
    params['address'] = location
    params['city'] = '上海市'
    params['output'] = 'json'
    params['ak'] = '2jGsS7SwsqZqI8yw5ZFjWq63'
    url_params = urllib.urlencode(params)
    baiduApi = apiStem + url_params      #print url_params
    #print baiduApi
    c=urllib.urlopen(baiduApi)
    addressLocation = json.loads(c.read())
    #print addressLocation
    try:
        print addressLocation["result"]["location"]["lat"],',',addressLocation["result"]["location"]["lng"]
    except Exception, e:
        print "Exception"

if __name__ == '__main__':
    locations = []
    try:
        file = open("D:\python\PyCharm 2016.1.2\workspace\git\pythonSpider\\files\locations.txt", 'r')
        context = file.readlines()
        locations = context
        file.close()
    except IOError as err:
        print(err)

    for location in locations:
        geoGrabBaidu(location)