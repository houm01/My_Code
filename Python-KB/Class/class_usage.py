#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01

# 先写一个通用的超类，定义员工默认的通用行为
class Employee:
    def computeSalart(self): ...
    def giveRaise(self): ...
    def promote(self): ...
    def retire(self): ...


'''
使用上面的通用行为后，就可以针对每个特定员工进行定制
也就是说，可以编写子类，定义每个员工不同的行为
例如有工程师有独特的薪资计算规则
'''
class Engineer(Employee):
    def computeSalary(self): ...   # 可以在子类中只取代上面超类的一种方法


# 建立员工所属的员工类种类的实例，从而使其获得正确的行为
bob = Employee()
mel = Employee()

# 当我们想查看员工薪资时，可以根据创建这个对象的类来计算，这也是基于继承搜索的原理
company = [bob, mel]
for emp in company:
    print(emp.computeSalart())