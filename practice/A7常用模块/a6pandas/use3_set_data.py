# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/23 下午4:26
IDE：PyCharm
描述：设置值
"""
import pandas as pd
import numpy as np

dates = pd.date_range('20180101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['第一列','第二列','第三列','第四列'])

# 设置index=2，columns = 1的值设置为1111
df.iloc[2,2] = 1111
# 设置20180101，第二列的值为2222
df.loc['20180101','第二列'] = 2222

# 第一列大于8的全部列设置为0
df[df.第一列 > 8] = 0
# 同上，只改变第一列的数值
df.第一列[df.第一列 > 8] = 0
# 同上，改第二列的值为0（当第一列值大于8的情况）
df.第二列[df.第一列 > 8] = 0

# 加一行空列
df['第五列'] = np.nan
# 加上一行，和index对应，以设定值
df['第六列'] = pd.Series([11,22,33,44,55,66],index = pd.date_range('20180101',periods=6))
print(df)


