# -*- coding:utf-8 -*-
'''
找出一个目录下的所有文件名
'''

import os

files = os.listdir("/Users/wangyuxiang/Desktop/快牛金科")

for f in files:
    print(f)
