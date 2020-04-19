"""
这是第一个GUI程序实例。
"""

#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   firstGUI.py
@Time    :   2020/04/19 15:04:58
@Author  :   Liu baochang 
@Contact :   543730416@qq.com
@License :   (C)Copyright @令狐少侠
'''

# here put the import lib
import wx


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent = None, title = "第一个GUI程序！", size = (300, 180))
        self.Center()
        panel = wx.Panel(parent = self)
        self.statictext = wx.StaticText(parent = panel, pos = (110, 20))
        b = wx.Button(parent = panel, label = 'OK', pos = (100, 50))
        self.Bind(wx.EVT_BUTTON, self.on_click, b)

    def on_click(self, Event):
        print(type(Event))
        self.statictext.SetLabelText('Hellow, world.')

class MyAPP(wx.App):
    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()
        print('应用程序启动！')
        return True

    def OnExit(self):
        print('应用程序退出。')
        return 0

if __name__ == '__main__':
    app = MyAPP()
    app.MainLoop()