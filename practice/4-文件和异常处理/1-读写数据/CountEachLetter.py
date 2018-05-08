# -*- coding:utf-8 -*-
'''
编写程序，提示用户输入一个文件名然后统计在不计大小写的情况下每个字符的出现次数
实现步骤：
1. 将文件中的每行作为一个字符串读取
2. 使用字符串的lower()方法把大写字母换成小写字母
3. 创建一个含有26个整型值得名为counts的列表，每个值是对每个字母出现次数的统计。counts[0]统计字母a的出现次数，counts[1]统计字母b的出现次数，以此类推
4. 对于字符串中的每个字符，判断它是否是一个小写字母。如果是，将列表中相应的计数器+1
5. 最后，显示统计结果
'''
def main():
    filename = input("Enter a filename: ").strip()
    infile = open(filename, "r")

    counts = 26 * [0]  # 创建一个含有26个元素的列表且初始化为0
    for line in infile:  # 从文件中读取每一行，将字母全部转化为小写
        countLetters(line.lower(), counts)  # 然后将转化后的字符传递来调用countLetters

    for i in range(len(counts)):
        if counts[i] != 0:
            print(chr(ord('a') + i) + " appears " + str(counts[i]) + (" time" if counts[i] == 1 else " times"))

    infile.close()

def countLetters(line, counts):  # 函数countLetters检查line中的每个字符，如果它是一个小写字符，程序将列表counts对应的元素+1
    for ch in line:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1

main()