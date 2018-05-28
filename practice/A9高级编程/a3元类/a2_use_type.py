# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/5/27 下午10:07
IDE：PyCharm
描述：
你也可以传递三个参数type(<name>, <bases>, <dct>)调用type()：
<name>指定类名称，将成为该类的__name__属性。
<bases>指定继承类的基类元组，将成为该类的__bases__属性。
<dct>指定包含类主体定义的名称空间字典，将成为该类的__dict__属性
"""

'eg1----------'
Foo = type('Foo', (), {})
x1 = Foo()
print('eg1:\n',x1,'\n')
'''
等同于
class Foo:
    pass
'''


'eg2----------'
# <bases>是一个具有单个元素Foo的元组，指定了Bar继承的父类。一个名为attr的属性最初放置在命名空间字典中：
Bar = type('Bar', (Foo,), dict(attr=100))
x2 = Bar()
print('eg2:\n',x2.attr)
print(x2.__class__)
print(x2.__class__.__bases__,'\n')
'''
等同于
class Bar:
    attr = 100
'''

'eg3----------'
# 两个对象通过<dct>参数放置在命名空间字典中。第一个是属性attr，第二个是函数attr_val，该函数将成为已定义类的一个方法：
Cer = type(
    'Cer',
    (),
    {
        'attr':100,
        'attr_val':lambda x : x.attr
    }
)
x3 = Cer()
print('eg3:\n',x3.attr)
print(x3.attr_val(),'\n')
'''
等同于
class Cer:
    attr = 100
    def attr_val(self):
        return self.attr
'''


'eg4----------'
# 外部先定义了一个稍微复杂的函数f，然后在命名空间字典中通过函数名f分配给attr_val
def fff(obj):
    print('attr = ', obj.attr)

Der = type(
    'Der',
    (),
    {
        'attr':100,
        'attr_val':fff
    }
)
x4 = Der()
print('eg4:\n',x4.attr)
x4.attr_val(),'\n'
'''
等同于
def fff(obj):
    print('attr = ', obj.attr)

class Foo:
    attr = 100
    attr_val = fff
'''