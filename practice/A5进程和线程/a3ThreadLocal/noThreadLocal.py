# -*- coding:utf-8 -*-
'''
在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁
但是局部变量也有问题，就是在函数调用的时候，传递起来很麻烦

'''

def process_student(name):
    std = Student(name)
    # std是局部变量，但是每个函数都要用它，因此必须传进去
    do_task_1(std)
    do_task_2(std)

def do_task_1(std):
    do_subtask_1(std)
    do_subtask_2(std)

def do_task_2(std):
    do_subtask_2(std)
    do_subtask_2(std)

# 每个函数一层一层调用都这么传参数太过麻烦。用全局变量？也不行，因为每个线程处理不同的Student对象，不能共享。