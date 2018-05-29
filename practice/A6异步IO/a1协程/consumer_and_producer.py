# -*- coding:utf-8 -*-
'''
1、协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，
   因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。
2、不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，
   只需要判断状态就好了，所以执行效率比多线程高很多
3、多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能

Python对协程的支持是通过generator实现的
在generator中，我们不但可以通过for循环来迭代，还可以不断调用next()函数获取由yield语句返回的下一个值

'''

# 协程:生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高

def consumer():
    r = ''
    while True:
        # 2.consumer通过yield拿到传递的None，yield跳出
        n = yield r
        # 4.从上次跳出的位置，接着往下执行
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'
        # 5.从这里开始循环，到yield的时候，再跳出来

def producer(c):  # 生产者
    # 1.启动生成器，会跳到consumer
    c.send(None)
    # 3.接着往下执行，产生数据，通过c.send(n)，再切换到consumer
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        # 6.跳出来后，函数返回值是200 OK，所以往下执行，print出200 OK
        print('[PRODUCER] Consumer return: %s' % r)
        # 7.从这里开始循环前面的步骤，直到最后
    c.close()

c = consumer()
producer(c)

'''
注意到consumer函数是一个generator，把一个consumer传入produce后：

1、首先调用c.send(None)启动生成器；

2、然后，一旦生产了东西，通过c.send(n)切换到consumer执行；

3、consumer通过yield拿到消息，处理，又通过yield把结果传回；

4、produce拿到consumer处理的结果，继续生产下一条消息；

5、produce决定不生产了，通过c.close()关闭consumer，整个过程结束。

整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。
'''