# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/7/11 下午12:36
IDE：PyCharm
描述：使用多进程的方法，那就是内置模块futures中的ProcessPoolExecutor
"""
from practice.common.my_wrapper import out_wrapper
from concurrent import futures
from practice.A8爬虫.A1Spiderway.a2_spider_photos.spider_photos_normal import download_one,user_conf


@out_wrapper
def download_many():
    zzr = user_conf()
    with futures.ProcessPoolExecutor(len(zzr)) as executor:
        res = executor.map(download_one, zzr)
    return len(list(res))

if __name__ == '__main__':
    download_many()