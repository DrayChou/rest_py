#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, sys
# 判断python的版本然后import对应的模块
if sys.version < '3':
    from Tkinter import *
else:
    from tkinter imp

import datetime
import threading

minute = 60 * 1
Curtime = datetime.datetime.now()
print ("时间为：",Curtime)
Scrtime = Curtime + datetime.timedelta(0,minute,0)
print("目标时间：",Scrtime)

def wait():
    threading._sleep(minute)

def Stat():
    Dsttime = datetime.datetime.now()
    tmp = Dsttime - Scrtime + Scrtime
    print("当前时间：",tmp)

    if tmp == Dsttime:
        class App(Frame):
            def __init__(self,master = None):
                Frame.__init__(self,master)
                self.pack()
                myapp = App()
                myapp.master.title("时间到了")
                myapp.master.maxsize(150,0)
                myapp.mainloop()
    else:
        print("NO")

wait()
Stat()
