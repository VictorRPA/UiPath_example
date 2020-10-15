# coding:utf-8
import urllib, urllib2, base64
import ssl
import json
#/usr/bin/env python
#coding=utf8
 
import httplib
import md5
import urllib
import random	

def getOcr(scr='c:/tools/myPic.jpg'):
        access_token = getToken()
        url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token=' + access_token
        # 二进制方式打开图文件
        f = open(scr, 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img}
        params = urllib.urlencode(params)
        request = urllib2.Request(url, params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib2.urlopen(request)
        retString = response.read()
        words_result = json.loads(retString)['words_result']
        words_list = list()
        retString=''
        for words in words_result:
            Str=words['words']
            retString=retString+Str+'\n'	
        return retString
		
def getToken():
        # client_id 为官网获取的AK， client_secret 为官网获取的SK
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=GtLt1zq2AoMwqmCr6OORT3go&client_secret=0yLa39aUdf4UqWY8wUL68j0EZV7QjZKI'
        request = urllib2.Request(host)
        request.add_header('Content-Type', 'application/json; charset=UTF-8')
        response = urllib2.urlopen(request)
        retString = response.read()
        new_dict = json.loads(retString)
        retString = new_dict['access_token']
        return retString

#30天需要更新
#print(u'\u957f\u98ce\u7834\u6d6a\u4f1a\u6709\u65f6,')
#print getToken()
#print(getOcr())
