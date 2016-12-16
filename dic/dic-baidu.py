#/usr/bin/env python
#coding=utf8
 
import http.client
import hashlib
import urllib
import random
import json
import sys
from urllib import parse

appid = '20160922000029057'
secretKey = '2Dv2Qw9S0e7Z7zz7TrU9'
 
httpClient = None
myurl = '/api/trans/vip/translate'
q = parse.quote(sys.argv[1])
fromLang = 'en'
toLang = 'zh'
salt = random.randint(32768, 65536)

sign = appid+q+str(salt)+secretKey
m1 = hashlib.md5()
m1.update(sign.encode('utf8'))
sign = m1.hexdigest()
myurl = myurl+'?appid='+appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign

try:
    httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET', myurl)
 
    #response是HTTPResponse对象
    response = httpClient.getresponse()
    data = response.read().decode('utf8')
    data = json.loads(data)
    print(data['trans_result'][0]['dst'])
    
except Exception as e:
    print(e)
finally:
    if httpClient:
        httpClient.close()
