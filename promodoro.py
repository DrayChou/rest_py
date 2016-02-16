#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading,time,Tkinter,tkFont

class Timer(threading.Thread):
    def __init__(self,fn,args=(),sleep=0,lastDo=True):
        threading.Thread.__init__(self)
        self.fn = fn
        self.args = args
        self.sleep = sleep
        self.lastDo = lastDo
        self.setDaemon(True)

        self.isPlay = True
        self.fnPlay = False

    def __do(self):
        self.fnPlay = True
        apply(self.fn,self.args)
        self.fnPlay = False

    def run(self):
        while self.isPlay :
            time.sleep(self.sleep)
            self.__do()

    def stop(self):
        #stop the loop
        self.isPlay = False
        while True:
            if not self.fnPlay : break
            time.sleep(0.01)
        #if lastDo,do it again
        if self.lastDo : self.__do()

top=Tkinter.Tk()
ft=tkFont.Font(root=top,family = ('sans-serif'), size = 10)
#ft=tkFont.Font(root=top,size = 13)
#ft=None
top.title("Promodoro")
LEFT, Label = Tkinter.LEFT, Tkinter.Label # shortcut names
frame = Tkinter.Frame(top)
frame.pack(fill=Tkinter.X, side=Tkinter.BOTTOM)
label_line = Tkinter.Frame(frame, relief=Tkinter.RAISED, borderwidth=1)
label_line.pack(side=Tkinter.TOP, padx=2, pady=1)
Label(label_line, text=u"Today's tomato(es):", width=20, anchor="w", font=ft).pack(side=LEFT)

num = Tkinter.StringVar()
num_label = Label(label_line, textvariable=num, anchor="e", width=2, font=ft)
num.set("0")
num_label.pack(side=LEFT)

Label(label_line, text=u" | ", width=1, font=ft).pack(side=LEFT)
Label(label_line, text=u" time left:   ", width=14, anchor="w", font=ft).pack(side=LEFT)
Label(label_line, text=u"25m16s", width=8, anchor="e", font=ft).pack(side=LEFT)

num_label.bind("<Button-1>",lambda event:num.set(str(event.x)))

top.mainloop()
