# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/9/16 下午3:29
IDE：PyCharm
描述：封装和加载对象
可以对每个对象或者整个列表进行pickle，但基于链表结构的集合，无法做到。因此，应该采用一种策略，将
集合中的单个项写入到一个文件中，并且再通过文件输入来重新创建集合。
"""
import pickle

# 保存
lyst = [60, "hhhh", "1977"]
fileObj = open("item.dat", "wb")
for item in lyst:
    pickle.dump(item, fileObj)
fileObj.close()

# 读取(如果读到文件末尾会报错，因此加上报错）
lyst1 = list()
fileObj = open("item.dat", "rb")
while True:
    try:
        item = pickle.load(fileObj)
        lyst1.append(item)
    except EOFError:
        fileObj.close()
        break
print(lyst1)
