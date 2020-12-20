#!/usr/bin/env python3

import sys
from tkinter import *

widget = Button(None, text='Hello widget world', command=sys.exit)
widget.pack()
widget.mainloop()

