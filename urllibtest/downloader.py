"""
使用urllib库实现一个下载小程序。
"""

#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   downloader.py
@Time    :   2020/04/19 00:24:03
@Author  :   Liu baochang 
@Contact :   543730416@qq.com
@License :   (C)Copyright @令狐少侠
'''

# here put the import lib
import urllib.request

url = 'https://piccdn.luojilab.com/fe-oss/activity/MTU4NTI4MjQ2ODc0.jpeg'

with urllib.request.urlopen(url) as response:
    data = response.read()
    f_name = './urllibtest/to_get_knowledge.jpeg'
    with open(f_name, 'wb') as f:
        f.write(data)
        print('下载成功。')