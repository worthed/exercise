# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/20 上午11:16
IDE：PyCharm
描述：对象可变，数值和字符串不可变
"""
class Count:
    def __init__(self, count = 0):
        self.count = count

def main():
    c = Count() #count=0
    times = 0 #times = 0
    for i in range(100):
        increment(c, times)

    print("count is", c.count)
    print("times is", times)


def increment(c, times):#count=0，#times = 0

    # 像圆这样的可变对象参数，如果对象的内容在函数内被改变，则对象的原始值被改变
    c.count += 1 #循环100次，每循环一次，c.count对象改变，加到100

    # 像数字或字符串这样的不可变对象参数，函数外的对象的原始值并没有被改变
    times += 1 #times没变（不是Count中的参数，不变）

main()