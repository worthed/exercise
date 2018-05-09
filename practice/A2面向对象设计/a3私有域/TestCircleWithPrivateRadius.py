# -*- coding:utf-8 -*-
from CircleWithPrivateRadius import Circle
c = Circle(5)
c.getRadius()
c.__radius #直接调用会报错 AttributeError: 'Circle' object has no attribute '__radius'