'''
该程序将一个源文件(demo_1)的数据复制到目标文件(demo_2)，并统计文件的行数和字符数
按行读取：
line = infile.readline()
while line != '':
    line =inflie.readline()
'''
import os.path
import sys

def main():
    f1 = "demo_1.txt"
    f2 = "demo_2.txt"

    if os.path.isfile(f2):
        print(f2 + " already exists")
        sys.exit()

    infile = open(f1, "r")
    outfile = open(f2, "w")

    countLines = countChars = 0
    # 使用for循环来读取文件所有行
    for line in infile:
        countLines += 1
        countChars += len(line)
        outfile.write(line)

    print(countChars, "lines and", countChars, "chars copied")

    infile.close()
    outfile.close()

main()