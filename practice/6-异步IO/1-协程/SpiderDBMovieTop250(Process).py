# -*- coding:utf-8 -*-
'''
多进程带来的优点（cpu处理）并没有得到体现，反而创建和调度进程带来的开销要远超出它的正面效应，拖了一把后腿。即便如此，多进程带来的效益相比于之前单进程单线程的模型要好得多。
'''
import requests
from lxml import etree
from time import time
from concurrent.futures import ProcessPoolExecutor

url = 'https://movie.douban.com/top250'

def fetch_page(url):
    response = requests.get(url)
    return response

def fetch_content(url):
    response = fetch_page(url)
    page = response.content
    return page

def parse(url):
    page = fetch_content(url)
    html = etree.HTML(page)

    xpath_movie = '//*[@id="content"]/div/div[1]/ol/li'
    xpath_title = './/span[@class="title"]'
    xpath_pages = '//*[@id="content"]/div/div[1]/div[2]/a'

    pages = html.xpath(xpath_pages)
    fetch_list = []
    result = []

    for element_movie in html.xpath(xpath_movie):
        result.append(element_movie)

    for p in pages:
        fetch_list.append(url + p.get('href'))

    with ProcessPoolExecutor(max_workers=4) as executor:
        for page in executor.map(fetch_content, fetch_list):
            html = etree.HTML(page)
            for element_movie in html.xpath(xpath_movie):
                result.append(element_movie)

    for i, movie in enumerate(result, 1):
        title = movie.find(xpath_title).text
        print(i, title)

def main():
    start = time()
    parse(url)
    end = time()
    print("Cost {} seconds".format((end - start)))

if __name__ == '__main__':
    main()