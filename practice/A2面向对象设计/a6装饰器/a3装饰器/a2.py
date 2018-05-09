# -*- coding:utf-8 -*-
'''
然后我们试图记录下这个函数执行的总时间，那最简单的做法就是
'''

#原始侵入，篡改原函数
import time
def func():
    startTime = time.time()

    print("hello")
    time.sleep(1)
    print("world")
    endTime = time.time()

    msecs = (endTime - startTime)*1000
    print("time is %d ms" %msecs)

func()
