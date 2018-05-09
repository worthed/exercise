# -*- coding:utf-8 -*-
def main():
    a = A()
    a.print()

class A:
    def __init__(self, newS = 'welcome'):
        self.__s = newS

    def print(self):
        print(self.__s)

main()

#正确输出