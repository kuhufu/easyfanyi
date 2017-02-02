#/usr/bin/env python3
# coding=utf8
# pylint: disable=C0103

import http.client
import json
import sys
from urllib import parse

if len(sys.argv) < 2:
    print("FORM: dic <world>")
    sys.exit(0)
    
keyfrom = 'easyfanyi'
key = '1929637537'
q = parse.quote(sys.argv[1])
myurl = '/openapi.do'
myurl = myurl + '?keyfrom=' + keyfrom + '&key=' + \
        key + '&type=data&doctype=json&version=1.1&q=' + q
httpClient = None

try:
    httpClient = http.client.HTTPConnection('fanyi.youdao.com')
    httpClient.request('GET', myurl)

    # response是HTTPResponse对象
    response = httpClient.getresponse()
    data = response.read().decode('utf8')
    data = json.loads(data)
    if len(sys.argv) == 3:
        print(data['basic']['us-phonetic'])
    explains = data['basic']['explains']
    for x in explains:
        print(x)

except Exception as e:
    print(e)
finally:
    if httpClient:
        httpClient.close()
