# -*- coding:utf-8 -*-
class A:
    def __init__(self, i):
        self.__i = i

    def getI(self):
        return self.__i

def main():
    a = A(5)
    print(a.getI())

main()

'''
错误示例：
class A:
    def __init__(self, i):
        self.__i = i

def main():
    a = A(5)
    print(a.__i)

main()
'''