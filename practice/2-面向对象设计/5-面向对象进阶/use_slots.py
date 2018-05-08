# -*- coding: utf-8 -*-

class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称

s = Student()  # 创建新的实例
s.name = 'Michael'  # 绑定属性'name'
s.age = 25  # 绑定属性'age'

'''
如果此处绑定属性score   
s.score = 99  
由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误
'''

# ERROR: AttributeError: 'Student' object has no attribute 'score'
try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)


# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__

class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 99  # 由于是Student的子类，故Student的__slots__不起作用
print('g.score =', g.score)
