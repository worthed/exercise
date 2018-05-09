# -*- coding:utf-8 -*-
from TV import TV

def main():
    tv1 = TV()
    tv1.turnOn()
    tv1.setChannel(30)
    tv1.setVolumeLevel(3)

    tv2 = TV()
    tv2.turnOn()
    tv2.channelUp()
    tv2.channelUp()  #频道加了两次，因TV.py中channel初始为1，故结果为3
    tv2.volumelevelUp() #音量加了一次，因TV.py中volumelevel初始为1，故结果为2

    print("tv1的频道是", tv1.getChannel(), ",tv1的音量是", tv1.getVolumeLevel())
    print("tv2的频道是", tv2.getChannel(), ",tv2的音量是", tv2.getVolumeLevel())

main()