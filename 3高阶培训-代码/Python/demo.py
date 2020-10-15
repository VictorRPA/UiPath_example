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

appid = 'xxxxx' #你的appid
secretKey = 'xxxxxx' #你的密钥

httpClient = None
myurl = '/api/trans/vip/translate'
q = 'it is a big apple tree.'
fromLang = 'en'
toLang = 'zh'
salt = random.randint(32768, 65536)

sign = appid+q+str(salt)+secretKey
m1 = md5.new()
m1.update(sign)
sign = m1.hexdigest()
myurl = myurl+'?appid='+appid+'&q='+urllib.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
 
try:
    httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET', myurl)
    #response是HTTPResponse对象
    response = httpClient.getresponse()
    getString = response.read()
    words_result = json.loads(getString)['trans_result']
    retString=words_result[0]['dst']
    print retString
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()
