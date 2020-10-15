# coding:utf-8
import urllib, urllib2, base64
import json
import httplib
import md5
import random

def getTranslate(q = 'apple tree is so big'):
        appid = '20190817000327342' #你的appid
        secretKey = 'LeZpxe4RNPlerFQ2LwiX' #你的密钥
        httpClient = None
        myurl = '/api/trans/vip/translate'        
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
            response = httpClient.getresponse()
            getString = response.read()
            #{"from":"en","to":"zh","trans_result":[{"src":"apple treee is so big","dst":"\u82f9\u679c\u6811\u592a\u5927\u4e86"}]}
            words_result = json.loads(getString)['trans_result']
            retString=words_result[0]['dst']
            return retString
        except Exception, e:
            return e
        finally:
            if httpClient:
                httpClient.close()


#print getTranslate("have a nice day !")
