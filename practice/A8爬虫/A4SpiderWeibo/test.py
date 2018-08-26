# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/7/25 下午3:30
IDE：PyCharm
描述：
"""
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
headerss = {
'Accept':'application/json, text/plain, */*',
'MWeibo-Pwa':'1',
'Referer':'https://m.weibo.cn/p/index?containerid=2302835650995316_-_INFO&title=%25E5%259F%25BA%25E6%259C%25AC%25E8%25B5%2584%25E6%2596%2599&luicode=10000011&lfid=2302835650995316&featurecode=20000320',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
'X-Requested-With':'XMLHttpRequest'
}
cap = DesiredCapabilities.PHANTOMJS.copy()
for key, value in headerss.items():
    cap['phantomjs.page.customHeaders.{}'.format(key)] = value
browser = webdriver.PhantomJS(desired_capabilities=cap)
'''
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("Mozilla/5.0 (iPhone 84; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.8.0 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1")
chromedriver = "/Users/wangyuxiang/Downloads/chromedriver"
'''
#browser = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
browser.get("https://m.weibo.cn/p/index?containerid=2302835650995316_-_INFO&title=%25E5%259F%25BA%25E6%259C%25AC%25E8%25B5%2584%25E6%2596%2599&luicode=10000011&lfid=2302835650995316&featurecode=20000320")

#new_list = browser.find_element_by_xpath('//div[@id=\'app\']/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]')

#print(new_list)