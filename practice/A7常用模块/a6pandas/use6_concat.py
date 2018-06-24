# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/23 下午5:53
IDE：PyCharm
描述：合并
axis  (合并方向)
ignore_index  (重置index)
join  (合并方式)
join_axes  (依照axes合并)
append  (添加数据)
"""

import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])

print(df1)
print(df2)
print(df3)

# axis=0 竖向合并，axis=1 横向合并
# ignore_index=True ,index重新排序
res = pd.concat([df1,df2,df3],axis=0,ignore_index=True)
print(res)

# 当列名和index部分相同的情况
df11 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df22 = pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
print(df11)
print(df22)
# 使用concat合并，会产生None值，使用join=outer'效果类似
print(pd.concat([df11,df22],axis=0))
# join='inner',则会只合并相同列名的部分，其他的删除掉
print(pd.concat([df11,df22],axis=0,sort=False,join='inner'))
# 按照df11的index横向合并，df11没有的用列none代替，df22多的index会去掉（去掉join_axes,则不会去掉df22多余的index)
print(pd.concat([df11,df22],axis=1,join_axes=[df11.index]))

# append
res3 = df1.append([df2,df3],ignore_index=True)
print(res3)