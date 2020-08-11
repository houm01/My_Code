#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

from person import Person


class Manager(Person):
    def giveRaise(self, percent, bonus=0.1):
        self.pay *= (1.0 + percent + bonus)


if __name__ == '__main__':
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    print(tom.lastName())
    tom.giveRaise(.20)
    print(tom.pay)

# 这个代码有些问题，还未解决