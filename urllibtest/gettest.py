"""
通过使用Request对发送HTTP/HTTPS的GET请求
"""

#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   gettest.py
@Time    :   2020/04/18 23:43:52
@Author  :   Liu baochang 
@Contact :   543730416@qq.com
@License :   (C)Copyright @令狐少侠
'''

# here put the import lib
import urllib.request
import urllib.parse


url = 'http://www.51work6.com/service/mynotes/WebService.php'
params_dict = {'email' : '543730416@qq.com', 'type' : 'JSON', 'action' : 'query'}
params_str = urllib.parse.urlencode(params_dict)
print(params_str)

urlpa= url + '?' + params_str    # 将HTTP请求参数放在URL之后
print(urlpa)

# 封装一个Response对象
req = urllib.request.Request(urlpa)
with urllib.request.urlopen(req) as response:
    data = response.read()
    data_json = data.decode()
    print(data_json)


params_bytes = params_str.encode()
req = urllib.request.Request(url, params_bytes)
with urllib.request.urlopen(req) as response:
    data = response.read()
    data_json = data.decode()
    print(data_json)