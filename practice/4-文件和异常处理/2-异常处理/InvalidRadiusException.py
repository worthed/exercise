# -*- coding:utf-8 -*-
'''
定制异常
'''

class InvalidRadiusException(RuntimeError):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
