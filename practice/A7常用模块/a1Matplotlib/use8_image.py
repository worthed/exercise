# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/30 下午10:40
IDE：PyCharm
描述：图像
"""

import matplotlib.pyplot as plt
import numpy as np

a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3,3)
# origin='upper'代表的就是选择的原点的位置，和矩阵对应，lower，和矩阵相反
# interpolation  https://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html
plt.imshow(a, interpolation='nearest', cmap='bone', origin='upper')

# shrink参数，使colorbar（右侧的bar）的长度变短为原来的92%
plt.colorbar(shrink=.92)

plt.xticks(())
plt.yticks(())
plt.show()


