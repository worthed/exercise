# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/23 下午3:41
IDE：PyCharm
描述：选择数据
筛选、标签loc、序列iloc、混合ix、判断的选择
"""
import pandas as pd
import numpy as np

dates = pd.date_range('20180101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['第一列','第二列','第三列','第四列'])

# 打印某一列
print(df['第一列'],df.第一列)

# 分片处理 0-3行
print(df[0:3])
# 分片，2018-01-03:2018-01-05
print(df['20180103':'20180105'])

# 索引 = 20180103，对应的列
print(df.loc['20180103'])
# 索引分片选择
print(df.loc[:,['第一列','第二列']])
# 索引 = 20180103 对应的第一列和第二列
print(df.loc['20180103',['第一列','第二列']])


# 打印index = 3的数据  注意index从0开始的
print(df.iloc[3])
# index = 4，columns = 1  注意columns也是从0开始的
print(df.iloc[3,1])
# 切片 index 3到5的，第四行和第五行的，第二列和第三列的，  注意切片前取后不取
print(df.iloc[3:5,1:3])

# 前三行，第一列和第二列
print(df.ix[:3,['第一列','第二列']])

# 筛选第一列>8的数据
print(df[df.第一列 > 8])

