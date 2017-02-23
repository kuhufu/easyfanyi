#/usr/bin/env python3
# coding=utf8
# pylint: disable=C0103

import sys
import json
import http.client
from urllib import parse

if len(sys.argv) < 2:
    print("Usage: dic <world>")
    sys.exit(0)

keyfrom = 'easyfanyi'
key = '1929637537'
q = parse.quote(sys.argv[1])
myurl = '/openapi.do?keyfrom=' + keyfrom + '&key=' + \
        key + '&type=data&doctype=json&version=1.1&q=' + q
httpClient = None

try:
    httpClient = http.client.HTTPConnection('fanyi.youdao.com')
    httpClient.request('GET', myurl)
    response = httpClient.getresponse()
    data = response.read().decode()
    basic = json.loads(data)['basic']

    if len(sys.argv) == 3:
        print(basic['us-phonetic'])
    for x in basic['explains']:
        print(x)
except Exception as e:
    print(e)
finally:
    if httpClient:
        httpClient.close()
