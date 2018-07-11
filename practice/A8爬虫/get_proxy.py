# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/7/11 下午3:58
IDE：PyCharm
描述：获取代理
"""
import random
import requests
import time
import pymongo
from bs4 import BeautifulSoup

# 爬取代理的URL地址，选择的是西刺代理
url_ip = "http://www.xicidaili.com/nt/"

# 设定等待时间
set_timeout = 5

# 爬取代理的页数，2表示爬取2页的ip地址
num = 2

# 代理的使用次数
count_time = 5

headers = {
           'User-Agent':
           'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
           }

# 测试ip的URL
url_for_test = 'http://httpbin.org/ip'

def scrawl_xici_ip(num):
    """
    爬取代理ip地址
    :param num:爬取的页数
    :return: ip的列表
    """
    ip_list = []
    for num_page in range(1,num):
        url = url_ip + str(num_page)
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            content = response.text
            soup = BeautifulSoup(content,'lxml')
            trs = soup.find_all('tr', {'class':'odd'})
            for i in range(1,len(trs)):
                tr = trs[i]
                tds = tr.find_all('td')
                # tds[1].text  第二个td，ip地址
                # tds[2].text  第三个td，是端口
                ip_item = tds[1].text + ':' + tds[2].text
                ip_list.append(ip_item)
                ip_set = set(ip_list)  # 去重
                ip_list = list(ip_set)
            time.sleep(count_time) #等待时间
    return ip_list

def ip_test(url_for_test,ip_info):
    """
    :param url_for_test:测试网站
    :param ip_info:ip_list
    :return:测试爬取到的ip，测试成功则存入MongoDB
    """
    for ip_for_test in ip_info:
        # 设置代理
        proxies = {
            'http': 'http://' + ip_for_test,
            'https': 'https://' + ip_for_test,
                   }
        print(proxies)
        try:
            response = requests.get(url_for_test,headers=headers,proxies=proxies,timeout=10)
            if response.status_code == 200:
                ip = {'ip': ip_for_test}
                print(response.text)
                print('测试通过')
                write_to_MongoDB(ip)
        except Exception as e:
            print(e)
            continue

def write_to_MongoDB(proxies):
    """
    将测试通过的ip存入MongoDB
    :param proxies:代理ip
    :return:
    """
    client = pymongo.MongoClient(host='localhost',port=27017)
    db = client.PROXY
    collection = db.proxies
    result = collection.insert(proxies)
    print(result)
    print('存储MongoDB成功')


def get_random_ip():
    """
    随机取出一个ip
    :return: 可用的ip，不可用的会剔除掉
    """
    client = pymongo.MongoClient(host='localhost',port=27017)
    db = client.PROXY
    collection = db.proxies
    items = collection.find()
    length = items.count()
    ind = random.randint(0,length-1)
    useful_proxy = items[ind]['ip'].replace('\n','')
    proxy = {
        'http': 'http://' + useful_proxy,
        'https': 'https://' + useful_proxy,
            }
    response = requests.get(url_for_test,headers=headers,proxies=proxy,timeout=10)
    if response.status_code == 200:
        return useful_proxy
    else:
        print('此{ip}已失效'.format(ip=useful_proxy))
        collection.remove(useful_proxy)
        print('已经从MongoDB移除')
        get_random_ip()

def main():
    ip_info = []
    ip_info = scrawl_xici_ip(2)
    success_proxy = ip_test(url_for_test,ip_info)
    finally_ip = get_random_ip()
    print('取出的ip为：' + finally_ip)

if __name__ == '__main__':
    main()