#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

from tkinter import *
from tkinter.messagebox import showinfo


def reply():
    showinfo(title='popup', message='Button pressed!')


window = Tk()
button = Button(window, text='press', command=reply)
button.pack()
window.mainloop()