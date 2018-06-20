# -*- coding:utf-8 -*-
class Student(object):

    @property  # 把一个getter方法变成属性，只需要加上@property就可以了
    def score(self):
        return self._score

    @score.setter  # @property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60 # 实际转化为s.set_score(60)
s.score # 实际转化为s.get_score()
print(s.score)