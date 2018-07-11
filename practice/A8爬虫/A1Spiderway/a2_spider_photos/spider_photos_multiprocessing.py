# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/7/11 下午12:28
IDE：PyCharm
描述：
"""
from practice.common.my_wrapper import out_wrapper
from multiprocessing import Process
from practice.A8爬虫.A1Spiderway.a2_spider_photos.spider_photos_normal import download_one,user_conf

@out_wrapper
def download_many():
    zzr = user_conf()
    task_list = []
    for item in zzr:
        t = Process(target=download_one, args=(item,))
        t.start()
        task_list.append(t)
    [t.join() for t in task_list] # 等待下进程全部执行完毕（为了记录时间）

if __name__ == '__main__':
    download_many()
