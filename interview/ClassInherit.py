# -*- coding:utf-8 -*-
'''
类继承
'''

class A(object):
    def show(self):
        print("base show")

class B(object):
    def show(self):
        print("derived show")

obj = B()
obj.show()


# 如何调用类A的show方法？


obj.__class__ = A  #  __class__方法指向了类对象，只用给他赋值类型A，然后调用方法show，但是用完了记得修改回来
obj.show()
