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

def getOcr(scr='c:/tools/myPic.jpg',typeid=''):
        access_token = getToken()
        # access_token = '24.2f60707cd99a9f06279070038450bb72.2592000.1568293377.282335-16286559'
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
        #{"log_id": 4768305456752292435, "words_result_num": 5, "words_result": [{"words": "娓呰尪妤蜂綋瀛椾綋"}, {"words": "涓嶈鎵剧敓浜烘垨鑷繁涓嶅お浜?}, {"words": "瑙ｇ殑浜哄悎浣滈櫎闈炰綘宸茬粡鎷?}, {"words": "鏈夐┚寰¤繖绉嶅嵄闄╁悎浣滅殑缁忛獙"}, {"words": "涓庤兘鍔?}]}
        words_result = json.loads(retString)['words_result']
        retString=''
        for words in words_result:
            Str=words['words']
            #print(Str)
            retString=retString+Str+'\n'	
        return retString

def getTranslate(q = 'apple treee is so big',typeid=''):
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

        httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        response = httpClient.getresponse()
        getString = response.read()
        #{"from":"en","to":"zh","trans_result":[{"src":"apple treee is so big","dst":"\u82f9\u679c\u6811\u592a\u5927\u4e86"}]}
        words_result = json.loads(getString)['trans_result']
        retString=words_result[0]['dst']
        return retString
		
def getToken():
        # client_id 为官网获取的AK， client_secret 为官网获取的SK
        #API Key GtLt1zq2AoMwqmCr6OORT3go
        #Secret Key 0yLa39aUdf4UqWY8wUL68j0EZV7QjZKI
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=GtLt1zq2AoMwqmCr6OORT3go&client_secret=0yLa39aUdf4UqWY8wUL68j0EZV7QjZKI'
        request = urllib2.Request(host)
        request.add_header('Content-Type', 'application/json; charset=UTF-8')
        response = urllib2.urlopen(request)
        retString = response.read()
        #{
        #"refresh_token":"25.331e000435e2dde77cce78f6e3edf6d8.315360000.1873632787.282335-16286559",
        #"expires_in":2592000,
        #"session_key":"9mzdWEG00fekqCnwwI1u2AEM9Lcye1KRMnGRjPtTCM01aK641R25DBLKx+mimiu\/PHQLXIx0U9WcnfNLluTOfgkUl1hC6A==",
        #"access_token":"24.c1a870b6f6d880463d0caedf0f8c3660.2592000.1560864787.282335-16286559",
        #"scope":"public vis-ocr_ocr brain_ocr_scope brain_ocr_general brain_ocr_general_basic vis-ocr_business_license brain_ocr_webimage brain_all_scope brain_ocr_idcard brain_ocr_driving_license brain_ocr_vehicle_license vis-ocr_plate_number brain_solution brain_ocr_plate_number brain_ocr_accurate brain_ocr_accurate_basic brain_ocr_receipt brain_ocr_business_license brain_solution_iocr brain_ocr_handwriting brain_ocr_passport brain_ocr_vat_invoice brain_numbers brain_ocr_train_ticket brain_ocr_taxi_receipt vis-ocr_\u8f66\u8f86vin\u7801\u8bc6\u522b vis-ocr_\u5b9a\u989d\u53d1\u7968\u8bc6\u522b brain_ocr_vin brain_ocr_quota_invoice wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test\u6743\u9650 vis-classify_flower lpq_\u5f00\u653e cop_helloScope ApsMis_fangdi_permission smartapp_snsapi_base iop_autocar oauth_tp_app smartapp_smart_game_openapi oauth_sessionkey smartapp_swanid_verify smartapp_opensource_openapi smartapp_opensource_recapi",
        #"session_secret":"30ca1cdad5e7b8e41af0e4e98dc56daf"}
        new_dict = json.loads(retString)
        retString = new_dict['access_token']
        return retString

#30天需要更新
#print getToken()
#print(getOcr())
#print(u'\u957f\u98ce\u7834\u6d6a\u4f1a\u6709\u65f6,')
#print getTranslate()
