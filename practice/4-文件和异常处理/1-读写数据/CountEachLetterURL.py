# -*- coding:utf-8 -*-
'''
使用urlopen函数打开一个URL，并从网站上读取数据  http://www.yahoo.com
'''
import urllib.request

def main():
    url = input("Enter a URL for a file: ").strip()
    infile = urllib.request.urlopen(url)
    s = infile.read().decode() # 使用infile.read()从URL上读取的数据是比特形式的原始数据，调用decode()方法将原始数据转换为一个字符串

    counts = countLetters(s.lower())

    for i in range(len(counts)):
        if counts[i] != 0:
            print(chr(ord('a') + i) + " appears " + str(counts[i]) + (" time" if counts[i] == 1 else " times"))

def countLetters(s):  # 函数countLetters检查line中的每个字符，如果它是一个小写字符，程序将列表counts对应的元素+1
    counts = 26 * [0]  # 创建一个含有26个元素的列表且初始化为0
    for ch in s:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1
    return counts

main()

