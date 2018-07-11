# -*- coding:utf-8 -*-
'''

'''
import os
import requests
import time
import random
from lxml import etree

keyWord = input(f"{'Please input the keywords that you want to download :'}")

class SpiderWallhavenPic():

    def __init__(self):
        self.headers = {
                        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
                        }
        self.proxies = {
                        "http": "http://122.114.31.177:808",
                        }
        self.filePath = ('/Users/wangyuxiang/Downloads/Pic/'+ keyWord + '/')

    def creat_File(self):
        """
        新建本地的文件夹路径，用于存储网页、图片等数据
        :return:
        """
        filePath = self.filePath
        if not os.path.exists(filePath):
            os.makedirs(filePath)

    def get_pageNum(self):
        """
        由于数字是夹在形如：1,985 Wallpapers found for “dog”的string中，
        所以需要用个小函数，提取字符串中的数字保存到列表numlist中，再逐个拼接成完整数字
        :return: 总页面数，用totalPagenum记录
        """
        total = ""
        url = ("https://alpha.wallhaven.cc/search?q={}&categories=111&purity=100&sorting=relevance&order=desc").format(keyWord)
        html = requests.get(url,headers = self.headers,proxies = self.proxies)
        selector = etree.HTML(html.text)
        pageInfo = selector.xpath('//header[@class="listing-header"]/h1[1]/text()')
        string = str(pageInfo[0])
        numlist = list(filter(str.isdigit,string))
        for item in numlist:
            total += item
        totalPagenum = int(total)
        return totalPagenum

    def main_fuction(self):
        self.creat_File()
        count = self.get_pageNum()  # 总图片数
        print("We have found:{} images!".format(count))
        times = int(count/24 + 1)  # 总页面数
        j = 1
        for i in range(times):
            pic_Urls = self.getLinks(i+1)
            for item in pic_Urls:
                self.download(item,j)
                j += 1

    def getLinks(self,number):
        """
        :param number: 给定number的页面中所有图片的链接
        :return: List形式返回图片链接
        """
        url = ("https://alpha.wallhaven.cc/search?q={}&categories=111&purity=100&sorting=relevance&order=desc&page={}").format(keyWord,number)
        try:
            html = requests.get(url,headers = self.headers,proxies = self.proxies)
            selector = etree.HTML(html.text)
            pic_Linklist = selector.xpath('//a[@class="jsAnchor thumb-tags-toggle tagged"]/@href')
        except Exception as e:
            print(repr(e))
        return pic_Linklist

    def download(self,url,count):
        string = url.strip('/thumbTags').strip('https://alpha.wallhaven.cc/wallpaper/')
        html = 'http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-' + string + '.jpg'
        pic_path = (self.filePath + keyWord + str(count) + '.jpg' )
        try:
            pic = requests.get(html,headers = self.headers)
            f = open(pic_path,'wb')
            f.write(pic.content)
            f.close()
            print("Image:{} has been downloaded!".format(count))
            time.sleep(random.uniform(0,2))
        except Exception as e:
            print(repr(e))

if __name__ == '__main__':
    spider = SpiderWallhavenPic()
    spider.main_fuction()