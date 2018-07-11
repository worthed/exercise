# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/7/5 下午2:54
IDE：PyCharm
描述：
"""
import os
import requests

# 创建一个文件夹
os.makedirs('./img/', exist_ok=True)
# 用os.chdir('F:/')就可以改变存储的位置

IMAGE_URL = "https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png"
r = requests.get(IMAGE_URL)
with open('./img/image2.png', 'wb') as f:
    f.write(r.content)


# 在下载大文件, 比如视频时. requests 下一点保存一点, 而不是要全部下载完才能保存
r = requests.get(IMAGE_URL, stream=True)
with open('./img/image3.png', 'wb') as f:
    for chunk in r.iter_content(chunk_size=32):
        f.write(chunk)