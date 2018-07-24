# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/5/29 下午12:34
IDE：PyCharm
描述：用yield实现协程
"""
# 为什么第二次调用next打印None呢？
'''
yield语句默认返回None。当第一次调用next方法时，生成器函数开始执行，执行到yield表达式为止，
但此时赋值操作并为执行。

代码中，在第一次调用next的时候，echo生成了1。
第二次调用next的时候，yield表达式的值赋给了n，n此时变成None了，再次yield n的时候就自然生成None了
'''

'eg1----------'
def echo(n):
    while True:
        n = yield n
g = echo(1)
print(next(g))
print(next(g))


'eg2----------'
def func():
    while True:
        print("before yield")
        x = yield
        print("after yield:",x)

g = func()
print('eg2 ：')
next(g) # 程序运行到yield并停在该处,等待下一个next
g.send('first_send') # 给yield发送值1,这个值被赋值给了x，并且打印出来,然后继续下一次循环停在yield处
g.send('second_send') # 给yield发送值2,这个值被赋值给了x，并且打印出来,然后继续下一次循环停在yield处
next(g) # 没有给x赋值，执行print语句，打印出None,继续循环停在yield处
'''
解释：
1、第一次调用next的时候，程序从函数最开始处运行，打印出before yield
2、向下执行到yield处，停在该处
3、接下来，向生成器send('first_send')。send在这里起到两个作用:
一个是将参数值赋给yield的返回值，然后该返回值赋给了变量x；
一个是继续程序的执行，直到下一次遇到yield停下来（第二个功能和next类似。其实，next 就相当于 send(None) )
4、执行了 send('first_send') 后，x被赋值给yield的返回值，即send的参数first_send，并继续往下执行，打印出了
after yield: first_send
5、新的一轮，继续执行程序，回到循环的开始，向下执行，打印出before yield
6、再次遇到yield，停在该处，等待下一次send或next的调用。
7、向生成器send('second_send')。这里的步骤和 send('first_send') 相同，打印出下面两条后，在yield处停住。
接着打印出after yield: second_send
8、进行第三轮，before yield
9、执行 next(g)，x被赋值为yield表达式的返回值，也就是None，继续向下执行，打印出after yield: None
10、再次回到循环的开始，向下执行，打印出before yield程序运行结束
'''

'eg3----------'
class Server:

    services = [
        {'active': False, 'protocol': 'ftp', 'port': 21},
        {'active': True, 'protocol': 'ssh', 'port': 22},
        {'active': True, 'protocol': 'http', 'port': 21},
    ]

    def __iter__(self):

        for service in self.services:
            if service['active']:
                yield service['protocol'], service['port']
s = Server()
for i in s.__iter__():
    print(i)
