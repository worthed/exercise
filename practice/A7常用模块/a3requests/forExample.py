# -*- coding:utf-8 -*-
'''

'''
import requests

# GET访问
r1 = requests.get('https://www.douban.com/') # 豆瓣首页
responsecode = r1.status_code  # 请求结果码
responsebody = r1.text # response body

# POST请求
r2 = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
# requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数
params = {'key': 'value'}
r3 = requests.post(url, json=params) # 内部自动序列化为JSON

# 带参数的URL
r4 = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
geturl = r4.url
# 检测编码
encodingtype = r4.encoding
# 用content属性获得bytes对象
bytes = r4.content

# JSON格式
r5 = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
json = r5.json()

# 传入HTTP Header
r6 = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
headertext = r6.text

# 获取响应头
r7.headers
r8.headers['Content-Type']

# Cookie
r9.cookies['ts']

# 在请求中传入Cookie
cs = {'token': '12345', 'status': 'working'}
r10 = requests.get(url, cookies=cs)

# 指定超时，传入以秒为单位的timeout参数
r11 = requests.get(url, timeout=2.5)