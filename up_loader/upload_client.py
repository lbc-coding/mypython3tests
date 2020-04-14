"""
这是一文件上传客户端程序
"""

#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   upload_client.py
@Time    :   2020/04/13 23:39:38
@Author  :   Liu baochang 
@Contact :   543730416@qq.com
@License :   (C)Copyright @令狐少侠
'''

# here put the import lib
import socket


HOST = '127.0.0.1'
PORT = 8889
f_name = 'shaoheng.jpg'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((HOST, PORT))

    with open(f_name, 'rb') as f:
        b = f.read()
        s.sendall(b)
        print('客户端上传数据完成。')