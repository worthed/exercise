# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/5/28 下午5:55
IDE：PyCharm
描述：容器、迭代器、生成器、yield
"""

'eg1----------容器（container）'
# 大多数的容器都是可迭代对象，可以使用某种方式访问容器中的每一个元素
'a' in {'a', 'b', 'c'} # 输出 True
'a' in {'a': 1, 'b': 2} # 输出 True
'a' in set(['a', 'b', 'c']) # 输出 True

'eg2----------迭代器（iterator）'
# 实现了__iter__和__next__方法的对象都称为迭代器。
# 迭代器是一个有状态的对象，在调用next() 的时候返回下一个值，如果容器中没有更多元素了，则抛出StopIteration异常。
'-1-'
a = ['a', 'b', 'c']
it = a.__iter__()
print('eg1: \n',next(it))
print(next(it))
print(next(it))
# print(next(it)) # 容器中没有更多元素了，抛出StopIteration异常
'-2-更好地理解迭代器的内部运行机制'
class Fib:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.curr, self.prev = self.prev + self.curr, self.curr
        return self.curr

fib = Fib()
for i in range(10):
    print('eg2 : ', next(fib))


'eg3----------生成器和yield'
# 生成器其实是一种特殊的迭代器，但是不需要像迭代器一样实现__iter__和__next__方法，只需要使用关键字yield就可以
def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        curr, prev = prev + curr, curr

f = fib()
# fib 函数中没有 return 关键字。当运行 f = fib() 的时候，它返回的是一个生成器对象。
# 在调用 fib() 的时候并不会运行 fib 函数中的代码，只有在调用 next() 的时候才会真正运行其中的代码。
for i in range(10):
    print('eg3 : ', next(f))


'eg4----------比较使用方法'
# 使用了生成器，在调用函数的时候不会一次性生成所有的元素，而是在每次调用 next() 才生成一个元素
def generate_square1(n):
    i = 0
    while i < n:
        yield i * i
        i += 1
result = generate_square1(10)
print('eg4 : \n', list(result))
# 未使用生成器
def generate_square2(n):
    i = 0
    result = []
    while i < n:
        result.append(i * i)
        i += 1
    return result

result = generate_square2(10)
print(result)
