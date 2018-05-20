# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/5/20 下午9:30
IDE：PyCharm
描述：利用上下文管理器同时管理多个资源
"""
# 读取一个文件的内容，经过处理以后，写入到另外一个文件中
with open('output.txt') as source:
    with open('target.txt', 'w') as target:
        target.write(source.read())

# 也可以写成如下这样，更简洁
with open('output.txt') as source, open('target.txt', 'w') as target:
    target.write(source.read())