'''
在文件末尾添加数据
'''
def main():
    outfile = open("Info.txt", "a")
    outfile.write("\nPython is interpreted\n")
    outfile.close()

main()