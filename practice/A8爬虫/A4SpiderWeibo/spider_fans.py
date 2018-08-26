# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/7/24 上午11:21
IDE：PyCharm
描述：
抓取粉丝列表，微博有限制，只能抓取少量的，于是抓取微博留言的用户（有互动的）

"""
import requests
import json
import time
import random
from  support.common.log.Log import CommonLog
import pandas as pd
from selenium import webdriver

# 获取微博的id
comment_parameter = []
# 评论url，存放weibo_url
comment_url = []

#获取每条微博的id值
url = 'https://m.weibo.cn/api/container/getIndex?uid=1773294041&luicode=10000011&lfid=100103type%3D1%26q%3D%E7%8E%8B%E8%8F%8A&\featurecode=20000320&type=uid&value=1773294041&containerid=1076031773294041'

c_r = requests.get(url)
for i in range(2,3):
# for i in range(2,11):
    c_parameter = (json.loads(c_r.text)["data"]["cards"][i]["mblog"]["id"])
    comment_parameter.append(c_parameter)

#获取每条微博评论url
c_url_base = 'https://m.weibo.cn/api/comments/show?id='
for parameter in comment_parameter:
    #for page in range(1,101):#提前知道每条微博只可抓取前100页评论
    for page in range(1, 5):  # 测试，只抓前5条
        c_url = c_url_base + str(parameter) + "&page=" + str(page)
        comment_url.append(c_url)
print(comment_url)

user_id = []#用来存放user_id
comment = []#用来存放comment
for url in comment_url:
    u_c_r = requests.get(url)
    try:
        #for m in range(0, 10):  # 提前知道每个url会包含9条用户信息,通过返回查询
        for m in range(0, 1):  # 提前知道每个url会包含9条用户信息,通过返回查询
            one_id = json.loads(u_c_r.text)["data"]["data"][m]["user"]["id"]
            user_id.append(one_id)
            one_comment = json.loads(u_c_r.text)["data"]["data"][m]["text"]
            comment.append(one_comment)
            time.sleep(random.randint(1,2))
            print(comment)
    except:
        CommonLog.info('%s 解析出错'%url)


containerid = []
user_base_url = "https://m.weibo.cn/api/container/getIndex?type=uid&value="
for id in set(user_id):#需要对user_id去重
    containerid_url = user_base_url + str(id)
    try:
        con_r = requests.get(containerid_url)
        one_containerid = json.loads(con_r.text)["data"]['tabsInfo']['tabs'][0]["containerid"]
        containerid.append(one_containerid)
    except:
        containerid.append(0)


#这里需要设置headers以及cookie模拟登陆feature = []#存放用户基本信息
feature = []#存放用户基本信息
id_lose = []#存放请求失败id
user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
#user_agent = 'Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
headers = {"User-Agent":user_agent}
headerss = {
'Accept':'application/json, text/plain, */*',
'MWeibo-Pwa':'1',
'Referer':'https://m.weibo.cn/p/index?containerid=2302835650995316_-_INFO&title=%25E5%259F%25BA%25E6%259C%25AC%25E8%25B5%2584%25E6%2596%2599&luicode=10000011&lfid=2302835650995316&featurecode=20000320',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
'X-Requested-With':'XMLHttpRequest'
}
m = 1
for num in zip(user_id,containerid):
    url = "https://m.weibo.cn/api/container/getIndex?uid={0}&luicode=10000011&lfid=100103type%3D1%26q%3D&featurecode=20000320&type=uid&value={1}&containerid={2}".format(str(num[0]),str(num[0]),str(num[1]))
    try:
        r = requests.get(url,headers = headerss)
        print(r.text)
        feature.append(json.loads(r.text)["data"]["cards"][0]["card_group"][1]["scheme"].split("  "))
        print("个人信息页面".format(feature))
        url1 = feature[0][0]
        print(url1)
        response = requests.get(url1,headers = headerss)
        print(response.text)
        m = m + 1
        time.sleep(1)#设置睡眠一秒钟，防止被封
    except:
        id_lose.append(num[0])

#将featrue建立成DataFrame结构便于后续分析
user_info = pd.DataFrame(feature,columns = ["性别","年龄","星座","国家城市"])
print(user_info)