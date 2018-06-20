# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/5/28 下午10:26
IDE：PyCharm
描述：
异常捕获的顺序:
一般在捕获异常的时候建议先捕获子类的异常，后捕获父类的异常。
这样，在有异常发生时，python解释器会根据except声明的顺序进行匹配，在第一个匹配的地方就立即处理异常。
"""

import sys
class InvalidValue(Exception):
    pass
class InvalidAge(InvalidValue):
    pass
class InvalidWeight(InvalidValue):
    pass

class Person(object):
    def __init__(self):
        pass

    def set_age(self, age):
        if age < 0:
            raise InvalidAge()
        self.age = age

    def set_weight(self, weight):
        if weight <= 0:
            raise InvalidWeight()
        self.weight = weight

p = Person()
try:
    p.set_age(30)
    p.set_weight(-30)
except InvalidValue:
    sys.exit("Invalid value")
except InvalidAge:
    sys.exit("Age cannot be negative")
except InvalidWeight:
    sys.exit("Weight cannot be negative")
'''
例子会输出 Invalid value
这里InvalidWeight类继承自InvalidValue类，当抛出InvalidWeight异常的时候，
由于它是InvalidValue的子类，在except InvalidValue处就被捕获了，输出了Invalid value的消息，
而真正处理InvalidWeight异常的消息却被掩盖了。
'''


'''
应该把捕获子类的except语句放在捕获父类的except语句之前，就可以避免这样的问题。
p = Person()
try:
    p.set_age(30)
    p.set_weight(-30)
except InvalidAge:
    sys.exit("Age cannot be negative")
except InvalidWeight:
    sys.exit("Weight cannot be negative")
except InvalidValue:
    sys.exit("Invalid value")
'''