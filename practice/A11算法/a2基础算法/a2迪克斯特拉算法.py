# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/8/18 下午9:48
IDE：PyCharm
描述：
a1广度优先算法，是找出段数最少的路径，如果要找出最快的路径，则需要用到迪克斯特拉算法
迪克拉斯特拉算法用于每条边都有关联数字的图，这些数字成为权重，带权重的图成为加权图，不带的成为非加权图

要计算非加权图的最短路径，可用广度优先算法，而计算加权图的最短路径，则使用迪克斯特拉算法
但迪克斯特拉算法只适合有向无环图，同时，也不适合包含负权边的图，这种图找最短路径，可使用贝尔曼·福德算法
"""
# 示例：起点到a，6分钟，a到终点1分钟；起点到b2分钟，b到终点5分钟，b到a3分钟
# 要计算最优路径，需要3个散列表，随着算法的进行，会不断更新costs和parents
'''
一graph
起点：A：6
     B：2
A：  终点：1
B：  A：3
     终点：5
终点：  --

二costs
A：6
B：2
终点：无穷

三parents
A：起点
B：起点
终点：--
'''
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}  # 终点没有任何邻居

infinity = float("inf")  # 表示无穷大
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = [] # 用一个数组记录处理过的节点，因为对于同一节点，不用多次处理

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs: # 遍历所有节点
        cost = costs[node]
        if cost < lowest_cost and node not in processed: # 如果当前节点的开销更低切未处理过
            lowest_cost = cost  # 则将其视为开销最低的节点
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs) # 在未处理的节点中找出开销最小的节点
while node is not None: # while循环在所有节点都被处理过后结束
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys(): # 遍历当前节点的所有邻居
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost: # 如果经当前节点前往该邻居最近
            costs[n] = new_cost # 则更新该邻居的开销
            parents[n] = node # 同时将该邻居父节点设置为当前节点
    processed.append(node)  # 将当前节点标记为处理过
    node = find_lowest_cost_node(costs)  # 找出接下来要处理的节点，并循环

print(costs["fin"])
print(parents)

'''
1、
node = find_lowest_cost_node(costs) 
在costs中找出开销最小的节点： 节点B，开销未2
2、
cost = costs[node]
neighbors = graph[node]
获取该节点的开销和邻居，开销为2，邻居为B，B仍旧是一个散列表
3、
for n in neighbors.keys():
遍历邻居B，获取B的键值
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
4、
new_cost = cost + neighbors[n]
新的开销 = 节点B的开销2 + 从节点B到节点A的开销3 = 5
5、
if costs[n] > new_cost:
对新（起点到B再到A，5）旧（起点到A，6）开销的对比
5、
costs[n] = new_cost
如果新开销5笔旧开销6小，则把更新节点A的开销，从6变成5
parents[n] = node
这条新路线经节点B到节点A，故将节点A的父节点从起点改为节点B
parents = {}
parents["a"] = "b"
parents["b"] = "start"
parents["fin"] = None
6、
for n in neighbors.keys():
进行下一个for循环，下一个邻居是终点节点
7、
new_cost = cost + neighbors[n]
经节点B前往终点需要的新的开销 = 起点到B点的开销2 + B到终点的开销5 = 7
8、
if costs[n] > new_cost:
终点节点原来的开销为无穷大，比7大    
    costs[n] = new_cost
    因此设置终点节点的开销为7
    parents[n] = node
    父节点为B
costs["a"] = 5
costs["b"] = 2
costs["fin"] = 7

parents["a"] = "b"
parents["b"] = "start"
parents["fin"] = "b"

9、循环结束
processed.append(node)
因为B节点已经处理过，则标记为处理过
node = find_lowest_cost_node(costs) 
找要处理的节点，得到节点A
10、
cost = costs[node]
neighbors = graph[node]
获取A的开销5（参照8），和A的邻居-终点1
11、
for n in neighbors.keys():
A只有一个邻居，遍历一次
12、
new_cost = cost + neighbors[n]
新的开销 = 起点到节点A的开销5 + A到终点的开销1 = 6
13、
if costs[n] > new_cost:
原来的开销7比新的开销6大
costs[n] = new_cost
故更新终点的开销
parents[n] = node
更新父节点
costs["a"] = 5
costs["b"] = 2
costs["fin"] = 6

parents["a"] = "b"
parents["b"] = "start"
parents["fin"] = "a"
'''