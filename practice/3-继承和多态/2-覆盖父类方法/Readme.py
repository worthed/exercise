# -*- coding:utf-8 -*-
'''
子类从父类继承方法。有时，子类需要修改定义在父类中的方法的实现，称为方法覆盖（override）
为了覆盖父类的方法，子类中的方法必须使用与父类方法一样的方法。但需注意，如果子类中的方法在父类是私有的，那么这两个方法是完全不相关的，即使这两个方法有同样的方法名。
'''

class A:
    def __init__(self, i = 5):
        self.i = i

    def m1(self):
        self.i += 1

class B(A):
    def __init__(self, j = 0):
        super().__init__(3)
        self.j = j

    def m1(self):
        self.i += 1

def main():
    b = B()
    b.m1()
    print(b.i)
    print(b.j)

main()
