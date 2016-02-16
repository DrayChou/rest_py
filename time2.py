#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, sys
# 判断python的版本然后import对应的模块
if sys.version < '3':
    from Tkinter import *
else:
    from tkinter import *

def update_timeText():
    # Get the current time, note you can change the format as you wish
    current = time.strftime("%H:%M:%S")

    # Update the timeText Label box with the current time
    timeText.configure(text=current)

    # Call the update_timeText() function after 1 second
    root.after(1000, update_timeText)

root = Tk()
root.wm_title("Simple Clock Example")

# Create a timeText Label (a text box)
timeText = Label(root, text="", font=("Helvetica", 150))
timeText.pack()
update_timeText()
root.mainloop()
