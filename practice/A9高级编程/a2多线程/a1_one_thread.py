# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/5/26 下午9:25
IDE：PyCharm
描述：
"""
from time import sleep,ctime

def loop0():
    print('开始第一个loop方法：',ctime())
    sleep(4)
    print('结束第一个loop方法：',ctime())

def loop1():
    print('开始第二个loop方法：',ctime())
    sleep(2)
    print('结束第二个loop方法：',ctime())

if __name__ == '__main__':
    print('程序开始：',ctime())
    loop0()
    loop1()
    print('程序结束：',ctime())
