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
        # 创建内容面板，作为所有内容的容器
        panel = wx.Panel(parent = self)

        # 创建整体垂直布局管理器对象，用于管理所有空间或者布局管理器
        vbox = wx.BoxSizer(wx.VERTICAL)
        # 创建一个水平布局管理器，用于管理按钮
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.statictext = wx.StaticText(parent = panel, pos = (110, 15))
        b1 = wx.Button(parent = panel, label = 'Button1', pos = (100, 45), id = 10)
        b2 = wx.Button(parent = panel, label = 'Button2', pos = (100, 85), id = 11)
        self.Bind(wx.EVT_BUTTON, self.on_click, b1)
        self.Bind(wx.EVT_BUTTON, self.on_click, id = 11)

        # 将按钮装进水平布局管理器
        hbox.Add(b1, 0, wx.EXPAND | wx.BOTTOM, 5)
        hbox.Add(b2, 0, wx.EXPAND | wx.BOTTOM, 5)

        # 将静态文本框和hbox添加到垂直布局管理器
        vbox.Add(self.statictext, proportion = 2, flag = wx.FIXED_MINSIZE | wx.TOP | wx.CENTER, border = 10)
        vbox.Add(hbox, proportion = 1, flag = wx.CENTER)

        # 将内容面板设置为尺寸随垂直布局管理器
        panel.SetSizer(vbox)

    def on_click(self, Event):
        event_id = Event.GetId()
        print("id为{0}的按钮被点击。".format(event_id))
        print(type(Event))
        if event_id == 10:
            self.statictext.SetLabelText('Button1单击')
        else:
            self.statictext.SetLabelText('Button2单击')

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