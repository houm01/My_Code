# -*- coding: utf-8 -*-
# github: https://github.com/houm01


class Person():
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)


class Manager(Person):
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)
        # self.pay = int(self.pay * (1 + percent + bonus))


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    # print(bob.name.split()[-1])
    # sue.pay *= 1.10
    # print(sue.pay)
    tom = Manager('Tom Jones', 'mgr', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)
