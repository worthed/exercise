# -*- coding:utf-8 -*-
class TV:
    #__init__初始化程序为TV对象中的数据域创建实例变量channel,volumelevel和on    数据域也被称为实例变量
    def __init__(self):
        self.channel = 1
        self.volumelevel = 1
        self.on = False
    '''
    以上该区域为数据域，如需隐藏数据域可用：
    self.__channel = 1
    self.__volumelevel = 1
    self.__on = False
    使用私有域后，其他函数的调用
    '''

    def turnOn(self):
        self.on = True

    def turnOff(self):
        self.on = False

    def getChannel(self):
        return self.channel

    def setChannel(self, channel):
        if self.on and 1 <= self.channel <= 120:
            self.channel = channel

    def getVolumeLevel(self):
        return self.volumelevel

    def setVolumeLevel(self, volumelevel):
        if self.on and 1 <= self.volumelevel <= 7:
            self.volumelevel = volumelevel

    def channelUp(self):
        if self.on and self.channel < 120:
            self.channel += 1

    def channelDown(self):
        if self.on and self.channel > 1:
            self.channel -= 1

    def volumelevelUp(self):
        if self.on and self.volumelevel < 7:
            self.volumelevel += 1

    def volumelevelDown(self):
        if self.on and self.volumelevel > 1:
            self.volumelevel -= 1