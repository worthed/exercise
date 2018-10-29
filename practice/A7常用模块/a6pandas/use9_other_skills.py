# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/10/28 下午7:55
IDE：PyCharm
描述：
"""
import pandas as pd
import numpy as np

data = pd.Series(np.random.randn(1000), index=np.arange(1000))
print(data)

# 直接将pandans对象写入压缩格式，直接写入gzip、bz2、zip或xz压缩，
# 而不是将未压缩的文件存储在内存中并进行转换
data.to_json('df.json.gz', orient='records', lines=True, compression='gzip')

import os.path
print(os.path.getsize('df.json') / os.path.getsize('df.json.gz'))