#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

from tkinter import mainloop
from tkinter.messagebox import showinfo
from tkinter102 import MyGui


class CustomGui(MyGui):
    def reply(self):
        showinfo(title='popup', message='Outh!')


if __name__ == '__main__':
    CustomGui().pack()
    mainloop()