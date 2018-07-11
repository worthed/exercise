# -*- coding:utf-8 -*-
'''

'''
import requests

# GET访问
res1_1 = requests.get('https://www.douban.com/')
responsecode = res1_1.status_code  # 请求结果码
responsebody = res1_1.text # 返回body
# 带参数的get
param = {"wd": "Python"}  # 搜索的信息
res1_2 = requests.get('http://www.baidu.com/s', params=param)


# POST请求
data = {'firstname': 'mm', 'lastname': '22'}
url = 'http://pythonscraping.com/files/processing.php'
res2_1 = requests.post(url, data=data)
# json格式的post请求
# requests默认使用application/x-www-form-urlencoded对POST数据编码。
# 如果要传递JSON数据，可以直接传入json参数
params = {'key': 'value'}
res2_2 = requests.post(url, json=params) # 内部自动序列化为JSON

# 带参数的URL
res3 = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
# 获取url
# print(res3.url)
# 获取编码
# print(res3.encoding)
# 用content属性获得bytes对象
# print(res3.content)

# 获取JSON格式
res4 = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# print(res4.json())

# 获取响应头
# print(res4.headers)
# print(res4.headers['Content-Type'])

# 指定超时时间，传入以秒为单位的timeout参数
# res5 = requests.get(url, timeout=10)


# 上传图片
file = {'uploadFile': open('./image.png', 'rb')}
# res6 = requests.post('http://pythonscraping.com/files/processing2.php', files=file)


# 带cookies的请求
payload = {'username': 'Morvan', 'password': 'password'}
res7_1 = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
# print(res7_1.cookies.get_dict())

res7_2 = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=res7_1.cookies)
# print(res7_2.text)


# 带session的请求
session = requests.Session()
payload = {'username': 'Morvan', 'password': 'password'}
res8_1 = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
print(res8_1.cookies.get_dict())

res8_2 = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(res8_2.text)