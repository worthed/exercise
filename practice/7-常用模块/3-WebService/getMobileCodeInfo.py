# -*- coding:utf-8 -*-
'''
web service网址
'''

from suds.client import Client

# web service查询:http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx

# 电话号码归属地查询
url = 'http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl'
client = Client(url)
result = client.service.getMobileCodeInfo(mobileCode = '18018001800', userID = '')
print(result)
