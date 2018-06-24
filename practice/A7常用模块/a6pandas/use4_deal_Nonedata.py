# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/23 下午5:03
IDE：PyCharm
描述：处理丢失数据（含NaN的矩阵）
pd.dropna()
pd.fillna()
pd.isnull()
"""
import pandas as pd
import numpy as np

dates = pd.date_range('20180101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['第一列','第二列','第三列','第四列'])

# 设置为None
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan

# 丢掉数据
# axis=0，丢掉含none的行；axis=1，丢掉含none的列
# how=any，选定行（列）中有一个none值就丢掉；how=all，选定行（列）全部都是none的情况才会丢掉
df.dropna(axis=0,how='all')

# 填上none的数据
print(df.fillna(value=0))
# 判定value是否为none，是的话为True，反之为False
print(df.isnull())
# df中是否含有none，如果有的话返回为True
print(np.any(df.isnull()) == True)
print(df)

