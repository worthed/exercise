# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/7/11 下午3:58
IDE：PyCharm
描述：获取代理
优化成异步协程+多进程，放在云服务器上单独跑。
各个进程分别负责抓取、去重、验证和生成可用ip队列。
然后写一个接口从队列获取，用的时候直接调用接口就行。
"""
import random
import requests
import time
import pymongo
from bs4 import BeautifulSoup
from support.common.connect.connect_db.ConnectDB import localhost_query,localhost_insert_or_update
from fake_useragent import UserAgent


url_for_test = 'http://httpbin.org/ip'  # 测试ip的URL
headers = {'User-Agent': str(UserAgent().random)}

def scrawl_xici_ip(num):
    """
    爬取代理ip地址
    :param num: 爬取第x页
    :return: ip的列表
    """
    ip_list = []
    url_ip = "http://www.xicidaili.com/nt/"  # 爬取代理的URL地址，选择的是西刺代理
    for num_page in range(1,num+1):
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
            time.sleep(5) #等待时间
    return ip_list



def ip_test_for_save(url_for_test,ip_info):
    """
    测试爬取到的ip，测试成功则存入mysql
    :param url_for_test: 测试网站
    :param ip_info: ip_list
    :return:
    """
    for ip_for_test in ip_info:
        # 设置代理
        proxies = {
            'http': 'http://' + ip_for_test,
            'https': 'https://' + ip_for_test,
                   }
        try:
            response = requests.get(url_for_test,headers=headers,
                                    proxies=proxies,timeout=10)
            if response.status_code == 200:
                # ip = {'ip': ip_for_test}
                print(proxies,"可用")
                write_to_IPpool(proxies)
        except Exception as e:
            print(e)
            continue


def write_to_IPpool(proxies):
    """
    将测试通过的ip存入mysql
    :param proxies: 代理ip dict
    :return:
    """
    sql = "INSERT INTO proxy (proxy_info,proxy_status) VALUES (\"{0}\",'1');".format(proxies)
    localhost_insert_or_update(sql)


def select_from_IPpool():
    """
    随机取ip
    :return:
    """
    sql = "SELECT proxy_info FROM proxy WHERE proxy_status = '1' ORDER BY RAND() limit 1;"
    useful_proxy = eval(localhost_query(sql)[0][0])
    response = requests.get(url_for_test,headers=headers,
                            proxies=useful_proxy,timeout=10)
    if response.status_code == 200:
        return useful_proxy
    else:
        update_IPpool(change_state=0,proxies=useful_proxy)
        select_from_IPpool()


def delete_from_IPpool(proxies):
    """
    删除ip
    :param proxies: 代理ip dict
    :return:
    """
    sql = "DELETE FROM proxy WHERE proxy_info = \"{0}\"".format(proxies)
    localhost_insert_or_update(sql)


def update_IPpool(change_state,proxies):
    """
    更新ip池状态
    :param change_state: 想要变的状态，传1改为1(有效)，传0改为0(无效）
    :param proxies:
    :return:
    """
    if change_state == 1:
        sql = "update proxy set proxy_status = '1' where proxy_info = \"{0}\";".format(proxies)
        localhost_insert_or_update(sql)
    elif change_state == 2:
        sql = "update proxy set proxy_status = '0' where proxy_info = \"{0}\";".format(proxies)
        localhost_insert_or_update(sql)


def scrawl_proxy_and_save_main(num):
    """
    抓取第几页的ip并保存
    :param num: 第x页
    :return:
    """
    ip_info = scrawl_xici_ip(num)
    ip_test_for_save(url_for_test,ip_info)


if __name__ == '__main__':
    for i in range(1,10):
        scrawl_proxy_and_save_main(i)
    #print(select_from_IPpool())