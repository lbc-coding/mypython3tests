"""
Python的urllib库包含4个模块：
urllib.request模块：用于打开和读写URL资源。
urllib.error模块：包含了由于urllib.request引起的异常。
urllib.parse模块：用于解析URL。
urllib.robotparse模块：用于分析robot.txt文件。
"""
#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   pyurllib.py
@Time    :   2020/04/18 23:16:43
@Author  :   Liu baochang 
@Contact :   543730416@qq.com
@License :   (C)Copyright @令狐少侠
'''

# here put the import lib
import urllib.request


with urllib.request.urlopen('http://sina.com.cn/') as response:     # 返回一个file-like object
    data = response.read()
    html = data.decode()
    print(html)