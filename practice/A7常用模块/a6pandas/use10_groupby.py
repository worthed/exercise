# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/11/29 下午10:16
IDE：PyCharm
描述：使用pandas的聚合
"""

import pandas as pd
df = pd.DataFrame([[1,2,2],[1,4,5],[1,2,4],[1,6,3],[2,3,1],[2,4,1],[2,3,5],[3,1,1]],
                  columns=['A','B','C'])

gp = df.groupby(by=['A','B'])

print(gp.size())
# 由gp.size()得到的是可以mulitiindex Series，转化成DataFrame的结构
newdf=gp.size()
newdf.reset_index(name='times')
print(newdf)

