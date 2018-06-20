# -*- coding:utf-8 -*-
class TV:
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


if __name__ == '__main__':
    tv1 = TV()
    tv1.turnOn()
    tv1.setChannel(30)
    tv1.setVolumeLevel(3)

    tv2 = TV()
    tv2.turnOn()
    tv2.channelUp()
    tv2.channelUp()  # 频道加了两次，因TV.py中channel初始为1，故结果为3
    tv2.volumelevelUp()  # 音量加了一次，因TV.py中volumelevel初始为1，故结果为2

    print("tv1的频道是", tv1.getChannel(), ",tv1的音量是", tv1.getVolumeLevel())
    print("tv2的频道是", tv2.getChannel(), ",tv2的音量是", tv2.getVolumeLevel())
