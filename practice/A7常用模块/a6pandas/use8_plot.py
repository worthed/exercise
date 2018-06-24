# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/23 下午10:11
IDE：PyCharm
描述：数据可视化
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.Series(np.random.randn(1000), index=np.arange(1000))
data = data.cumsum()
# data.plot()
# plt.show()

data1 = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list("ABCD"))
data1 = data1.cumsum()
ax = data1.plot.scatter(x='A', y='B', color='DarkBlue', label="Class 1")
data1.plot.scatter(x='A', y='C', color='LightGreen', label='Class 2', ax=ax)
data1.plot()
plt.show()