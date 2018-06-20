# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/11 下午2:12
IDE：PyCharm
描述：在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改
"""

class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        # 为了限制score的范围，可以通过一个set_score()方法来设置成绩，
        # 再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
s.set_score(60)
s.get_score()
print(s.get_score())