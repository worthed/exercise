# -*- coding:utf-8 -*-
'''
将电视机作为一个例子。
每个电视机都是一个带有多个状态（即当前频道、当前音量、电源开或关，这些都是数据域所代表的电视机的属性）
和带有多个行为（调频道、调音量、打开/关闭，这些都是每个电视机对象用方法执行的动作）的对象

TestTV.py，是使用TV类创建两个对象的程序
'''

UML类图
TV
#数据域  数据域也被称为实例变量
channel: int
volumeLevel: int
on: bool

TV()  #构建一个默认的电视对象
turnOn: None
turnOff: None
getChannel: int
setChannel(channel: int): None
getVolumeLevel: int
setVolumeLevel(volumeLevel: int): None
channelUp: None
channelDown: None
volumelevelUp: None
volumelevelDown: None