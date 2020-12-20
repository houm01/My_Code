#!/usr/bin/env python3

import sys
from tkinter import *

widget = Button(None, text='Hello event world', command=(lambda: print('Hello lamba world') or sys.exit()))
widget.pack()
widget.mainloop()