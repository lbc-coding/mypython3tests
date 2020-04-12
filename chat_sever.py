"""
本程序提供一个聊天服务器端的服务程序。
"""

#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   chat_sever.py
@Time    :   2020/04/12 23:15:28
@Author  :   Liu baochang 
@Contact :   543730416@qq.com
@License :   (C)Copyright @令狐少侠
'''

# here put the import lib
 
import socket

# 创建一个socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 指定使用IPV4和TCP协议
s.bind(('', 8889))
s.listen()
print('服务器启动成功...')

# 等待客户端连接
conn, address = s.accept()
# 客户端连接成功
print(address)

# 从客户端接收数据
data = conn.recv(1024)
print('从客户端接受的消息是：{0}'.format(data.decode()))

# 给客户端发送数据
conn.send('你好！'.encode())

# 释放资源
conn.close()
s.close()