# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/30 下午10:57
IDE：PyCharm
描述：分割成几个小图
"""
import matplotlib.pyplot as plt

plt.figure()

# 将整个图像窗口分为2行2列, 当前位置为1
plt.subplot(2,2,1)
# 在第1个位置创建一个小图
plt.plot([0,1],[0,1])

# 将整个图像窗口分为2行2列, 当前位置为2
plt.subplot(2,2,2)
# 在第2个位置创建一个小图
plt.plot([0,1],[0,2])

# 图3
plt.subplot(223)
plt.plot([0,1],[0,3])
# 图4
plt.subplot(224)
plt.plot([0,1],[0,4])


# 不均匀的图

# 分为2行1列, 当前位置为1
plt.subplot(2,1,1)
plt.plot([0,1],[0,1])
'''
上一步中使用plt.subplot(2,1,1)将整个图像窗口分为2行1列, 第1个小图占用了第1个位置, 也就是整个第1行. 
这一步中使用plt.subplot(2,3,4)将整个图像窗口分为2行3列, 于是整个图像窗口的第1行就变成了3列, 
也就是成了3个位置, 于是第2行的第1个位置是整个图像窗口的第4个位置.
'''
plt.subplot(2,3,4) # 分为2行3列, 当前位置为4
plt.plot([0,1],[0,2])
plt.subplot(235)
plt.plot([0,1],[0,3])
plt.subplot(236)
plt.plot([0,1],[0,4])
plt.show()

