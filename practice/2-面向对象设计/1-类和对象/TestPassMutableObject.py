# -*- coding:utf-8 -*-
#不变对象和可变对象举例

from Circle import Circle

def main():
    #程序传递一个Circle对象myCircle和一个int对象n去调用printArea(myCircle,n),它打印一个半径分别为1，2，3，4，5所对应的面积的列表
    myCircle = Circle()
    n = 5
    printAreas(myCircle, n)

    print("\nRadius is", myCircle.radius)
    print("n is", n)

def printAreas(c, times):
    print("Radius \t\tArea")
    while times >= 1:
        print(c.radius, "\t\t", c.getArea())
        c.radius = c.radius + 1  #circle对象c的radius属性增加1。c.radius+1创建了一个新的int对象，并将他赋值给c.radius。
        #myCircle和c都指向同一个对象。当printArea函数完成后，c.radius是6,随意输出是6
        times = times - 1 #times-1创建一个新的int对象，它被赋值给times。在函数printArea之外，n还是5，所以，n的输出还是5

main()


'''
像数字或字符串这样的不可变对象参数，函数外的对象的原始值并没有被改变
像圆这样的可变对象参数，如果对象的内容在函数内被改变，则对象的原始值被改变
'''

'''
eg1:
class Count:

    def __init__(self, count = 0):
        self.count = count

def main():
    c = Count()
    times = 0
    for i in range(100):
        increment(c, times)

    print("count is", c.count)
    print("times is", times)

def increment(c, times):
    c.count += 1
    times += 1

main()

-----------------------------------
>>count is 100
>>times is 0
-----------------------------------

eg2:
class Count:

    def __init__(self, count = 0):
        self.count = count

def main():
    c = Count()
    n = 1
    m(c, n)

    print("count is", c.count)
    print("n is", n)

def m(c, n):
    c = Count(5)
    n = 3

main()

-----------------------------------
>>count is 0
>>n is 1
-----------------------------------

'''