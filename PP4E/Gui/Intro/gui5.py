#!/usr/bin/env python3

from tkinter import *
import os

class HelloButton(Button):
    def __init__(self, parent=None, **config):
        Button.__init__(self, parent, **config)
        self.pack()
        self.config(command=self.callback)
    
    def callback(self):
        print('Goodbye world...')
        self.quit()


if __name__ == "__main__":
    HelloButton(text='hello subclass world').mainloop()
    