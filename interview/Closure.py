# -*- coding:utf-8 -*-
'''
闭包
'''

# 写一个函数，接收整数参数n，返回一个函数，函数的功能是把函数的参数和n相乘并把结果返回

def mulby(num):
    def gn(val):
        return num * val

    return gn


zw = mulby(7)
print(zw(9))