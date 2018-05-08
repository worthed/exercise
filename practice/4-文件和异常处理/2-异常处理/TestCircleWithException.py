# -*- coding:utf-8 -*-
from CircleWithException import Circle
from InvalidRadiusException import InvalidRadiusException

try:
    c1 = Circle(5)
    print("c1's area is", c1.getArea())
    c2 = Circle(-5)
    print("c1's area is", c2.getArea())
    c3 = Circle(0)
    print("c1's area is", c3.getArea())
except InvalidRadiusException as ex:   # 当except子句捕获到异常时，这个异常对象就被赋给一个名为ex的变量，可以在后面使用这个对象
    print("The Radius", ex.radius, "is invalid")
except RuntimeError:
    print("Something is wrong")



