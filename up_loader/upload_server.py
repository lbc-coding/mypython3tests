"""
这是一个文件上传服务端程序。
"""

#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   upload_server.py
@Time    :   2020/04/13 23:20:00
@Author  :   Liu baochang 
@Contact :   543730416@qq.com
@License :   (C)Copyright @令狐少侠
'''

# here put the import lib
import socket


HOST = ''
PORT = 8889

f_name = 'shaoheng_copy.jpg'

# 创建socket对象 ，绑定主机地址、端口，建立监听
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(10)
    print('服务器启动...')


    while True:
        with s.accept()[0] as conn:
            # 创建字节序列对象列表，用于接收数据的缓冲区
            buffer = []
            while True:
                data = conn.recv(1024)
                if data:
                    # 将接受的数据添加到缓冲区
                    buffer.append(data)
                else:
                    # 没有接收到数据则退出
                    break
        # 将接受的字节序列对象合并为一字节序列对象
        b = bytes().join(buffer)
        with  open(f_name, 'wb') as f:
            f.write(b)

        print('服务器接收完成。')