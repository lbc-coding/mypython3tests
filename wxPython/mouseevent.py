"""
这是一个鼠标事件练习。
"""

#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   mouseevent.py
@Time    :   2020/04/19 23:21:30
@Author  :   Liu baochang 
@Contact :   543730416@qq.com
@License :   (C)Copyright @令狐少侠
'''

# here put the import lib
import wx


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent = None, title = "鼠标事件处理！", size = (400, 300))
        self.Center()
        self.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)
        self.Bind(wx.EVT_LEFT_UP, self.on_left_up)
        self.Bind(wx.EVT_MOTION, self.on_mouse_move)

    def on_left_down(self, evt):
        print('鼠标按下')

    def on_left_up(self, evt):
        print('鼠标释放')

    def on_mouse_move(self, event):
        if event.Dragging() and event.LeftIsDown():
            pos = event.GetPosition()
            print(pos)


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