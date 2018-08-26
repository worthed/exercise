# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/8/1 下午2:53
IDE：PyCharm
描述：http://www.dmoz.org/  测试网站spider
"""
import scrapy

class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ["chinadmoz.org"]
    start_urls = [
        "http://www.chinadmoz.org/subindustry/10/",
        "http://www.chinadmoz.org/subindustry/15/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
