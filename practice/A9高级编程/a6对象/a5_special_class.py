# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/5 下午10:58
IDE：PyCharm
描述：类的特殊成员
__doc__表示类的描述信息
# __module__ 表示当前操作的对象在那个模块
# __class__     表示当前操作的对象的类是什么
# __call__ 对象后面加括号，触发执行
# __dict__ 类或对象中的所有成员
# __str__ 如果一个类中定义了__str__方法，那么在打印 对象 时，默认输出该方法的返回值
"""

'-1-'
# __doc__表示类的描述信息
class Foo1:
    """ 描述类信息，这是用于看片的神奇 """

    def func(self):
        pass
print(Foo1.__doc__)
#输出：类的描述信息


'-2-'
# __module__ 表示当前操作的对象在那个模块
# __class__     表示当前操作的对象的类是什么
class C:
    def __init__(self):
        self.name = 'wupeiqi'
from practice.A9高级编程.a6对象.a5_test import C

obj2 = C()
print(obj2.__module__)  # 输出 practice.A9高级编程.a6对象.a5_test，即：输出模块
print(obj2.__class__)     # 输出 <class 'practice.A9高级编程.a6对象.a5_test.C'>，即：输出类

'-3-'
# __call__ 对象后面加括号，触发执行
class Foo3:

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print('__call__')

obj3 = Foo3() # 执行 __init__
obj3()       # 执行 __call__


'-4-'
# __dict__ 类或对象中的所有成员
class Province:

    country = 'China'

    def __init__(self, name, count):
        self.name = name
        self.count = count

    def func(self, *args, **kwargs):
        print('func')

# 获取类的成员，即：静态字段、方法、
print(Province.__dict__)
# 输出：{'country': 'China', '__module__': '__main__', 'func': <function func at 0x10be30f50>, '__init__': <function __init__ at 0x10be30ed8>, '__doc__': None}

obj4_1 = Province('HeBei',10000)
print(obj4_1.__dict__)
# 获取 对象obj1 的成员
# 输出：{'count': 10000, 'name': 'HeBei'}

obj4_2 = Province('HeNan', 3888)
print(obj4_2.__dict__)
# 获取 对象obj1 的成员
# 输出：{'count': 3888, 'name': 'HeNan'}

'-5-'
# __str__ 如果一个类中定义了__str__方法，那么在打印 对象 时，默认输出该方法的返回值
class Foo5:
    def __str__(self):
        return 'wupeiqi'

obj5 = Foo5()
print(obj5)
# 输出：wupeiqi

'-6-'
# __getitem__、__setitem__、__delitem__
# 用于索引操作，如字典。以上分别表示获取、设置、删除数据
class Foo6(object):

    def __getitem__(self, key):
        print('__getitem__',key)

    def __setitem__(self, key, value):
        print('__setitem__',key,value)

    def __delitem__(self, key):
        print('__delitem__',key)


obj6 = Foo6()

result = obj6['k1']      # 自动触发执行 __getitem__
obj6['k2'] = 'wupeiqi'   # 自动触发执行 __setitem__
del obj6['k1']           # 自动触发执行 __delitem__


'-7-'
# __getslice__、__setslice__、__delslice__
# 该三个方法用于分片操作，如：列表
class Foo7(object):

    def __getslice__(self, i, j):
        print('__getslice__',i,j)

    def __setslice__(self, i, j, sequence):
        print('__setslice__',i,j)

    def __delslice__(self, i, j):
        print('__delslice__',i,j)

obj7 = Foo7()

# obj7[-1:1]                   # 自动触发执行 __getslice__，无此类
obj7[0:1] = [11,22,33,44]    # 自动触发执行 __setslice__
del obj7[0:2]                # 自动触发执行 __delslice__