# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/7/11 下午2:42
IDE：PyCharm
描述：
"""
import time
from threading import Thread
from practice.A8爬虫.A1Spiderway.a3_spider_wallhaven_pic.SpiderWallhavenPic import SpiderWallhavenPic

class SpiderWallhavenPic_Thread(SpiderWallhavenPic):

    def __init__(self):
        super().__init__()

    def main_fuction(self):
        self.creat_File()
        count = self.get_pageNum()
        print("We have found:{} images!".format(count))
        times = int(count/24 + 1)
        j = 1
        start = time.time()
        for i in range(times):
            pic_Urls = self.getLinks(i+1)
            start2 = time.time()
            threads = []
            for item in pic_Urls:
                t = Thread(target = self.download, args = [item,j])
                t.start()
                threads.append(t)
                j += 1
            for t in threads:
                t.join()
            end2 = time.time()
            print('This page cost：',end2 - start2,'s')
        end = time.time()
        print('Total cost:',end - start,'s')

if __name__ == '__main__':
    spider = SpiderWallhavenPic_Thread()
    spider.main_fuction()