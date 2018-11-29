# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/23 下午7:29
IDE：PyCharm
描述：
merge合并
依据一组key合并
依据两组key合并
indicator -- 指示器
依据index合并
解决overlapping的问题
"""
import pandas as pd
import numpy as np

# 一个key的情况
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                                  'A': ['A0', 'A1', 'A2', 'A3'],
                                  'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                                    'C': ['C0', 'C1', 'C2', 'C3'],
                                    'D': ['D0', 'D1', 'D2', 'D3']})

print(left)
print(right)
print(pd.merge(left,right,on='key'))

# 2个key，默认how=ineer
left1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                             'key2': ['K0', 'K1', 'K0', 'K1'],
                             'A': ['A0', 'A1', 'A2', 'A3'],
                             'B': ['B0', 'B1', 'B2', 'B3']})
right1 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                              'key2': ['K0', 'K0', 'K0', 'K0'],
                              'C': ['C0', 'C1', 'C2', 'C3'],
                              'D': ['D0', 'D1', 'D2', 'D3']})
print(left1)
print(right1)
# how = left，right，inner，outer
# 合并，key1和key2相等（left取index 0，2，2；right取 index 0，1，2）的行才合并
print(pd.merge(left1,right1,on=['key1','key2'],how='inner'))
# left和right的key1.key2都合并，没有的value用none代替
print(pd.merge(left1,right1,on=['key1','key2'],how='outer'))

# indicator 给一个直观的显示，显示出merge的方式
df1 = pd.DataFrame({'col1':[0,1], 'col_left':['a','b']})
df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
print(df1)
print(df2)
print(pd.merge(df1, df2, on='col1', how='outer', indicator=True))
# indicator列的名字
print(pd.merge(df1, df2, on='col1', how='outer', indicator='indicator_column'))


# merged by index
left2 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                                  'B': ['B0', 'B1', 'B2']},
                                  index=['K0', 'K1', 'K2'])
right2 = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                                     'D': ['D0', 'D2', 'D3']},
                                      index=['K0', 'K2', 'K3'])
print(left2)
print(right2)
# left_index and right_index
print(pd.merge(left2, right2, left_index=True, right_index=True, how='outer'))
print(pd.merge(left2, right2, left_index=True, right_index=True, how='inner'))


# handle overlapping
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
print(boys)
print(girls)
# 使用_下斜杠，命名列名，age变成age-boy，age-girl
print(pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='inner'))


