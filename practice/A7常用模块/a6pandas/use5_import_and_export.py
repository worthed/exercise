# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/23 下午5:38
IDE：PyCharm
描述：导入和到处
"""
import pandas as pd
import numpy as np

data = pd.read_csv('Student.csv',header=0,encoding='utf-8',sep=",")
print(data)

data.to_pickle('Student.pickle')