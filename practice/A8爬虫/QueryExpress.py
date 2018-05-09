# -*- coding:utf-8 -*-
'''

'''
import json
import requests
def searchPackage():
    # 输入运单号码。  eg：VB40641457651
    packageNum = input('请输入运单号码：')
    url1 = 'http://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text=' + packageNum
    # 用url1查询运单号对应的快递公司
    companyName = json.loads(requests.get(url1).text)['auto'][0]['comCode']
    # 再用url2查询和运单号、快递公司来查询快递详情，结果是一个json文件，用dict保存在resultdict中。
    url2 = 'http://www.kuaidi100.com/query?type=' + companyName + '&postid=' + packageNum
    # 还有个temp字段加不加都可以。如：'&temp=0.9829438147420106'
    print('时间↓                             地点和跟踪进度↓\n')
    packageName = json.loads(requests.get(url2).text)['data']
    for item in packageName:
        print(item['time'], item['context'])


searchPackage()

# url1-json
'''
    {
    "comCode":"",
    "num":"VB40641457651",
    "auto":[
        {
            "comCode":"jd",
            "id":"",
            "noCount":2887632,
            "noPre":"VB40",
            "startTime":""
        }
    ]
}
'''

# url2-json
'''
{
    "message":"ok",
    "nu":"VB40641457651",
    "ischeck":"1",
    "condition":"F00",
    "com":"jd",
    "status":"200",
    "state":"3",
    "data":[
        {
            "time":"2018-03-05 11:22:53",
            "ftime":"2018-03-05 11:22:53",
            "context":"货物已完成配送，感谢您选择京东配送",
            "location":""
        },
        {
            "time":"2018-03-05 09:17:51",
            "ftime":"2018-03-05 09:17:51",
            "context":"配送员开始配送，请您准备收货，配送员，詹东月，手机号，18986248076",
            "location":""
        },
        {
            "time":"2018-03-05 05:54:13",
            "ftime":"2018-03-05 05:54:13",
            "context":"货物已分配，等待配送",
            "location":""
        },
        {
            "time":"2018-03-05 05:54:12",
            "ftime":"2018-03-05 05:54:12",
            "context":"货物已到达【武汉花山站】",
            "location":""
        },
        {
            "time":"2018-03-04 14:50:24",
            "ftime":"2018-03-04 14:50:24",
            "context":"货物已完成分拣，离开【武汉亚一分拣中心】",
            "location":""
        },
        {
            "time":"2018-03-04 12:56:56",
            "ftime":"2018-03-04 12:56:56",
            "context":"货物已完成分拣，离开【武汉外单分拣中心】",
            "location":""
        },
        {
            "time":"2018-03-04 12:54:39",
            "ftime":"2018-03-04 12:54:39",
            "context":"货物已到达【武汉外单分拣中心】",
            "location":""
        },
        {
            "time":"2018-03-03 19:14:11",
            "ftime":"2018-03-03 19:14:11",
            "context":"货物已完成分拣，离开【南通分拨中心】",
            "location":""
        },
        {
            "time":"2018-03-03 18:55:39",
            "ftime":"2018-03-03 18:55:39",
            "context":"货物已到达【南通分拨中心】",
            "location":""
        },
        {
            "time":"2018-03-03 14:12:01",
            "ftime":"2018-03-03 14:12:01",
            "context":"货物已交付京东物流",
            "location":""
        }
    ]
}
'''