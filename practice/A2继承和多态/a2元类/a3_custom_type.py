# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/5/27 下午10:29
IDE：PyCharm
描述：
自定义元类。元类可以很容易地作为一种“寻找解决问题的方案”，通常不需要创建自定义元类。
如果手头上的问题能够以更简单的方式解决，那或许就应该采用。
"""

'eg1----------'
class Aoo:
    pass
a = Aoo()
'''
表达式Foo()创建一个新的类Foo的实例。
当解释器遇到Foo()，将按以下顺序进行解析：
1、调用Foo父类的__call__()方法。由于Foo是标准的新式类，它的父类是type元类，所以type的__call__()方法被调用。
2、__call__()方法按以下顺序进行调用：
ps:如果Foo没有定义__new__()和__init__()，那么将调用Foo父类的默认方法;如果Foo定义这些方法，就会覆盖来自父类的方法
__new__()
__init__()
'''


'eg2----------'
# 类似于这样的代码通常会出现在__init__()方法中，不会出现在__new__()方法里，这个例子仅为演示目的而设计
def new(cls):
    x = object.__new__(cls)
    x.attr = 100
    return x

class Boo():
    pass

Boo.__new__ = new
b1 = Boo()
print('eg1: ', b1.attr)


'eg3----------'
# 定义派生于type的元类
class Meta(type):  # 头部定义class Meta(type):指定了Meta派生自type。既然type是元类，那Meta也是一个元类。
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.attr = 100
        return x
'''
重新自定义了Meta的__new__()方法。因为不可能直接对type元类进行此类操作。__new__()方法执行以下操作：
1、经由super()指代的（type）元类的__new__()方法实际创建一个新的类
2、将自定义属性attr分配给类，并设置值为100
3、返回新创建的类
'''
class Coo(metaclass=Meta):
# 定义一个新类Foo，并指定其元类为自定义元类Meta，而不是标准元类type。可以通过在类定义中使用关键字metaclass完成
    pass
print('eg2: ', Coo.attr)