# -*- coding:utf-8 -*-
'''
设计一个类来建模栈。栈是以后进先出的方式保存数据的。
定义一个类来对对栈建模，并且使用列表来存储栈中的元素。有两种设计方式来设计一个对栈类。
方式一，使用继承，可以定义扩展list类的栈类
方式二，使用组合，可以在Stack类中创建一个列表
两种方式都很好，但使用组合更好，因为可定义一个完整的新栈类而不需要继承list类中不需要的和不适用的方法。
'''

from Stack import Stack

stack = Stack()

for i in range(10):
    stack.push(i)

while not stack.isEmpty():
    print(stack.pop(), end = "")