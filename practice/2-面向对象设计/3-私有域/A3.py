# -*- coding:utf-8 -*-

class A:
    def __init__(self, on):
        self.__on = not on

    def getOn(self):
        return self.__on

def main():
    a = A(False)
    print(a.getOn())

main()

'''
修改前
class A:
    def __init__(self, on):
        self.__on = not on

def main():
    a = A(False)
    print(a.on)

main()
'''