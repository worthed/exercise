# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/9/4 下午4:58
IDE：PyCharm
描述：只能使用类方法的例子
"""
class Fruit(object):
    total = 0

    def __init__(self, area="", category="", batch=""):
        self.area = area
        self.ccategory = category
        self.batch = batch

    @staticmethod
    def Init_Product(product_info):
        area, category, batch = map(int, product_info.split('-'))
        fruit = Fruit(area, category, batch)
        return fruit

    @classmethod
    def print_total(cls):
        print(cls.total)
        print(id(Fruit.total))
        print(id(cls.total))

    @classmethod
    def set(cls,value):
        print("calling class_method{0}{1}".format(cls,value))
        cls.total = value

class Apple(Fruit):
    pass

class Orange(Fruit):
    pass

apple1 = Apple(2, 5, 10)
orange1 = Orange.Init_Product("3-3-9")

print("apple1 is instance of Apple:"+str(isinstance(apple1, Apple)))
print("orange1 is instance of Orange:"+str(isinstance(orange1, Orange)))
# isinstance(orange1, Orange) 返回的是false，因为静态方法实际相当于一个定义在类里面的函数，
# Init_Product返回的实际是Fruit的对象，所以它不会是Orange的实例。
# Init_Product的功能类似于工厂方法，能够根据不同的类型返回的类的实例，因此使用静态方法并不能获得
# 期望的结果，类方法才是正确的解决方案


# 修改后的代码
class Fruit2(object):
    total = 0

    def __init__(self, area="", category="", batch=""):
        self.area = area
        self.ccategory = category
        self.batch = batch

    @classmethod
    def Init_Product(cls,product_info):
        area, category, batch = map(int, product_info.split('-'))
        fruit = cls(area, category, batch)
        return fruit

    @classmethod
    def print_total(cls):
        print(cls.total)
        print(id(Fruit.total))
        print(id(cls.total))

    @classmethod
    def set(cls,value):
        print("calling class_method{0}{1}".format(cls,value))
        cls.total = value

class Apple2(Fruit2):
    pass

class Orange2(Fruit2):
    pass

apple2 = Apple2(2, 5, 10)
orange2 = Orange2.Init_Product("3-3-9")

print("apple1 is instance of Apple:"+str(isinstance(apple2, Apple2)))
print("orange1 is instance of Orange:"+str(isinstance(orange2, Orange2)))



# 静态方法的用处：判断输入的合法性
# 其实，声明静态方法和类方法都可以，甚至可以作为定义在类外部的函数。但定义成静态方法，代码较为清晰。
# 定义在类中，较之外部函数，能够更有效的将代码组织起来，提高代码的可维护性。当然，如果有一组独立的
# 方法，将其定义在一个模块中，通过模块来访问这些方法也是一个不错的选择。
def is_input_valid(product_info):
    area, category, batch = map(int, product_info.split('-'))
    try:
        assert 0 <= area <= 10
        assert 0 <= category <= 15
        assert 0 <= batch <= 99
    except AssertionError:
        return False
    return True