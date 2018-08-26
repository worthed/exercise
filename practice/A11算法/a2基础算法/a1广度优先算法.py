# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/8/18 下午9:20
IDE：PyCharm
描述：找出两样东西之间的最短距离
如：
国际跳棋ai，计算最少走多少步就可以获胜
拼写检查器，计算最少编辑多少个地方就可将错拼的单词改成正确的单词，如将readed改为reader需要编辑一个地方
根据你的人际关系网络找到关系最近的医生
"""
from collections import deque

# 广度优先，其基础是建立在散列表之上
# 示例，从you的朋友中找到thom_mango，芒果经销商
graph = {}
# 你的朋友
graph["you"] = ["alice","bob","claire"]

# 你朋友的朋友
graph["bob"] = ["anuj","peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom_mango","jonny"]

# # 你朋友的朋友的朋友
graph["anuj"] = []
graph["peggy"] = []
graph["thom_mango"] = []
graph["jonny"] = []

# 使用队列判断这人是否是芒果经销商（名字中带有mango），队列保持先进先出，
# 先进入队列核对是否是芒果经销商的，先出来，不同于调用栈，是后进先出

def person_is_mango_seller(name):
    return name[-5:] == 'mango'

def search(name):
    search_queue = deque()  # 创建一个队列
    search_queue += graph["you"]  # 将你的朋友加入到这个搜索队列中
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:  # 这个人没被搜索过才检查，避免朋友的朋友有重复的情况
            if person_is_mango_seller(person):
                print(person + " is mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person) # 标记已搜索过
    return False

search("you")
