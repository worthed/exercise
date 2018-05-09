# -*- coding:utf-8 -*-
class A:
    def __init__(self, i):
        self.__i = i

def geti(self):
    return self.__i

def main():
    a = A(5)
    print(a.__i)


main()
