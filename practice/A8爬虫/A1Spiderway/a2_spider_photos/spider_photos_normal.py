# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/7/11 上午11:14
IDE：PyCharm
描述：
"""
import os
import uuid
# uuid 生成唯一识别码，用于命名filename
import requests
from bs4 import BeautifulSoup
from io import BytesIO
from practice.common.my_wrapper import out_wrapper


# 保存图片
def save_flag(img, filename):
    path = os.path.join('down_photos', filename)
    with open(path, 'wb') as fp:
        fp.write(img)

# 下载一个图片
def download_one(url):
    image = requests.get(url)
    save_flag(image.content, ''.join([str(uuid.uuid4()),'.jpg']))

# 返回30个图片的url
def user_conf():
    url = 'https://unsplash.com/'
    ret = requests.get(url)
    soup = BeautifulSoup(ret.text, "lxml")
    zzr = soup.find_all('img')
    ret = []
    num = 0
    for item in zzr:
        if item.get("src").endswith('80') and num < 10:
            num += 1
            ret.append(item.get("src"))
    return ret


@out_wrapper
def download_many():
    zzr = user_conf()
    for item in zzr:
        download_one(item)


if __name__ == '__main__':
    download_many()
