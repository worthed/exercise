# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/4 下午10:42
IDE：PyCharm
描述：字段，类中的静态字段和普通字段
"""

# 通过类创建对象时，如果每个对象都具有相同的字段，那么就使用静态字段
class Province:

    # 静态字段，属于类
    country = '中国'

    def __init__(self, name):
        # 普通字段，属于对象
        self.name = name

# 直接访问普通字段,普通字段在每个对象中都要保存一份
obj = Province('河北省')
print(obj.name)

# 直接访问静态字段,静态字段在内存中只保存一份
print(Province.country)

