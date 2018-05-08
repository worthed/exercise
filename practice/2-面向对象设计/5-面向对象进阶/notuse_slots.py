# -*- coding:utf-8 -*-
class Student(object):
    pass


class GraduateStudent(Student):
    pass

# 1-给实例绑定一个属性
s = Student()  # 创建新的实例
s.name = 'Michael'  # 绑定属性'name'
print(s.name)

# 2-给实例绑定一个方法
def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25) # 调用实例方法
s.age # 测试结果
print(s.age)

# 3-但是，给一个实例绑定的方法，对另一个实例是不起作用的
'''
s2 = Student() # 创建新的实例
s2.set_age(25) # 尝试调用方法  

会报错：
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'set_age'
'''

#为解决3中的问题，给所有实例都绑定方法，可以给class绑定方法
def set_score(self, score):
    self.score = score
Student.set_score = set_score

#给class绑定方法后，所有实例均可调用
s.set_score(100)
s.score
print(s.score)
s.age # 测试结果
print(s.age)

s2 = Student()
s2.set_score(99)
s2.score
print(s2.score)

'''
通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现

但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。为了达到限制的目的，Python允许在定义class的时候，
定义一个特殊的__slots__变量，来限制该class实例能添加的属性
'''