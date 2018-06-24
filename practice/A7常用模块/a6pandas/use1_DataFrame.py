# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/23 下午3:02
IDE：PyCharm
描述：DataFrame基础
"""
import pandas as pd
import numpy as np

data1 = pd.Series([1,2,3,4,np.nan,55,1])
# print(data1)

data2 = pd.date_range(start='2018-02-26',periods=6)
# print(data2)

# 打印6行4列，index为data2中随机生成的日期，列名为自定义的
data3 = pd.DataFrame(np.random.randn(6,4),index=data2,columns=['第一列','第二列','第三列','第四列'])
# print(data3)

data4 = pd.DataFrame({'第一列':1.,
                      '第二列':pd.Timedelta('20130102'),
                      '第三列':pd.Series(1,index=list(range(4)),dtype='float32'),
                      '第四列':np.array([3]*4,dtype='int32'),
                      '第五列':pd.Categorical(['test','train','test','train']),
                      '第六列':'foo'})
print(data4)
# 打印每列的数组类型
print(data4.dtypes)
# 打印索引
print(data4.index)
# 列名
print(data4.columns)
# 每一行的value
print(data4.values)
# 描述dataframe数字的基本数学运算，如方差、平均等
print(data4.describe())
# 转换下，行列交换
print(data4.T)


# 排序
# 按照列名，ascending的True或者False决定正向还是逆向
print(data4.sort_index(axis=1,ascending=False))
# 按照index倒序
print(data4.sort_index(axis=0,ascending=False))
# values排序
print(data4.sort_values(by='第五列'))