#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01


class C2():
    ...

class C3():
    ...

class C1(C2, C3):
    def setname(self, who):
        self.name = who


I1 = C1()
I2 = C1()
I1.setname('bob')
I2.setname('mel')
print(I1.name)
print(I2.name)