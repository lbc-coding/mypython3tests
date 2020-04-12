"""
这是一个聊天客户端服务程序。
"""

#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   chat_client.py
@Time    :   2020/04/12 23:33:05
@Author  :   Liu baochang 
@Contact :   543730416@qq.com
@License :   (C)Copyright @令狐少侠
'''

# here put the import lib
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 链接服务器
s.connect(('127.0.0.1', 8889))

# 给服务器发送数据
s.send(b'Hello!')

# 从服务器接收数据
data = s.recv(1024)
print('从服务器接受的消息是：{0}'.format(data.decode()))

# 释放资源
s.close()