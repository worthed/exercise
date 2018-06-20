# -*- coding:utf-8 -*-
#eg1
print("eg1:")
class A1:
    def __init__(self, i1 = 5):
        self.i1 = i1

    def m1(self):
        self.i1 += 1

    def __str__(self):
        return str(self.i1)

x = A1(8)
print(x)

#----------------------------------------------------eg2

print("\neg2:")
class A2:
    def __new__(self):
        print("A2's __new__() invoked")  #invoked 调用

    def __init__(self):
        print("A2's __init__() invoked")

class B2(A2):
    def __new__(self):
        print("B2's __new__() invoked")

    def __init__(self):
        print("B2's __init__() invoked")

b2 = B2()
a2 = A2()



#----------------------------------------------------eg3

print("\neg3:")
class A3:
    def __new__(self):
        self.__init__(self)
        print("A3's __new__() invoked")

    def __init__(self):
        print("A3's __init__() invoked")

class B3(A3):
    def __new__(self):
        self.__init__(self)
        print("B3's __new__() invoked")

    def __init__(self):
        print("B3's __init__() invoked")

b3 = B3()
a3 = A3()



#----------------------------------------------------eg4

print("\neg4:")
class A4:
    def __init__(self):
        print("A4's __init__() invoked")

class B4(A4):
    def __init__(self):
        print("B4's __init__() invoked")

b4 = B4()
a4 = A4()

#----------------------------------------------------eg4

print("\neg5:")
class A5:
    def __init__(self, i5):
        self.i5 = i5

    def __str__(self):
        return "A5"


class B5(A5):
    def __init__(self, i5, j5):
        super().__init__(i5)
        self.j5 = j5


b5 = B5(1, 2)
a5 = A5(1)
print(a5)
print(b5)



#----------------------------------------------------eg6

print("\neg6:")
class A6:
    def __init__(self, i6):
        self.i6 = i6

    def __str__(self):
        return "A6"

    def __eq__(self, other):
        return self.i6 == other.i6

x = A6(1)
y = A6(1)
print(x == y)