'''
该程序将一个源文件的数据复制到目标文件，并统计文件的行数和字符数

程序经常需要从一个文件中读取全部数字，可以使用read()方法读取，然后将它作为一个字符串返回，也可以使用readlines()方法
读取，然后将它作为一个字符串列表返回。但对于文件很大的时候，需要换用方法，可编写循环语句(for or while)每次读取文件的一行，
持续读取下一行直到文件末端。
eg：
line = infile.readline()
while line != '':
    # Process the line here ...
    # Read next line
    line =inflie.readline()

'''
import os.path
import sys

def main():
    f1 = input("Enter a source file: ").strip()
    f2 = input("Enter a target file: ").strip()

    if os.path.isfile(f2):
        print(f2 + " already exists")
        sys.exit()

    infile = open(f1, "r")
    outfile = open(f2, "w")

    countLines = countChars = 0
    for line in infile:  # 使用for循环来读取文件所有行
        countLines += 1
        countChars += len(line)
        outfile.write(line)

    print(countChars, "lines and", countChars, "chars copied")

    infile.close()
    outfile.close()

main()