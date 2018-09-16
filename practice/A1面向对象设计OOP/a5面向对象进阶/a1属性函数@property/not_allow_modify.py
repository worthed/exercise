# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/9/16 下午8:46
IDE：PyCharm
描述：
"""
##不推荐
class Clock(object):
    def __init__(self):
        self.__hour = 1
    def setHour(self, hour):
        if 25 < self.__hour < 0: self.__hour = hour
        else: raise Exception
    def getHour(self):
        return self.__hour

##推荐
class Clock2(object):
    def __init__(self):
        self.__hour = 1
    def __setHour(self, hour):
        if 25 < self.__hour < 0: self.__hour = hour
        else: raise Exception
    def __getHour(self):
        return self.__hour
    hour = property(__getHour, __setHour)

