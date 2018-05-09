# -*- coding:utf-8 -*-
'''
r 为了读取打开一个文件
w 为了写入打开一个文件，如果文件以及存在，它的内容就会被销毁
a 打开一个文件从文件末尾追加数据
rb 为读取二进制数据打开文件
wb 为写入二进制数据打开文件
'''
import os.path
if os.path.isfile("Presidents.txt"):   # 测试文件是否存在，防止已存在的文件中的数据被意外消除，应该在打开一个文件进行写操作之前检测该文件是否已经存在。

    print("Presidents.txt exists")

def main():
    outfile = open("Presidents.txt", "w")  #如果该文件不存在，那么open函数会创建一个新文件

    outfile.write("Wang\n")
    outfile.write("Qian\n")
    outfile.write("Sun\n")

    outfile.close()

main()