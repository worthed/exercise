# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/11/5 下午5:58
IDE：PyCharm
描述：
使用枚举类型代替字面量的好处：
提升代码可读性：所有人都不需要记忆某个神奇的数字代表什么
提升代码正确性：减少打错数字或字母产生 bug 的可能性
"""
from enum import IntEnum


class TripSource(IntEnum):
    FROM_WEBSITE = 11
    FROM_IOS_CLIENT = 12


def mark_trip_as_featured(trip):
    if trip.source == TripSource.FROM_WEBSITE:
        print(trip.source)

    elif trip.source == TripSource.FROM_IOS_CLIENT:
        print(trip.source)
    return trip.source

