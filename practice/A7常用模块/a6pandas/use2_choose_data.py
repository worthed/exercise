# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/23 下午3:41
IDE：PyCharm
描述：选择数据
筛选、标签loc、序列iloc、混合ix、判断的选择

loc， 即可以使用column名和index名进行定位，如：df.loc[‘image1’:‘image10’, ‘age’:‘score’]
iloc，即index locate 用index索引进行定位，所以参数是整型，如：df.iloc[10:20, 3:5]
ix，是混用型

"""
import pandas as pd
import numpy as np

dates = pd.date_range('20180101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['第一列','第二列','第三列','第四列'])

print(df)

'''选择行（注意切片必须要带两个，否则df会认为是取列而报错'''
# 分片处理 0-3行的所有列
print(df[0:3])
# 分片处理，第x行到第y行的所有列
print(df['20180103':'20180105'])


'''通过列名选择列'''
# 打印某一列
print(df['第一列'])


'''loc，使用column名和index名进行定位'''
# 索引 = 20180103，对应的列
print(df.loc['20180103'])
# 索引分片选择
print(df.loc[:,['第一列','第二列']])
# 索引 = 20180103 对应的第一列和第二列
print(df.loc['20180103',['第一列','第二列']])


'''iloc，index locate 用index索引进行定位'''
# 打印index = 3的数据  注意index从0开始的
print(df.iloc[3])
# index = 4，columns = 1  注意columns也是从0开始的
print(df.iloc[3,1])
# 切片 index 3到5的，第四行和第五行的，第二列和第三列的，  注意切片前取后不取
print(df.iloc[3:5,1:3])


'''ix，混合型定位'''
# 前三行，第一列和第二列
print(df.ix[:3,['第一列','第二列']])


'''筛选'''
# 筛选第一列>8的数据
print(df[df.第一列 > 8])

# 当第一列=8时的行
print(df.loc[df['第一列']==8])
# 当第一列 in (8,12) 时的行
print(df.loc[df['第一列'].isin([8,12])])
# 当第一列 not in (8,12) 时的行
print(df.loc[~df['第一列'].isin([8,12])])
# 当第一列=8并且第二列=9时的行
print(df.loc[(df['第一列']==8)&(df['第二列']==9)])
