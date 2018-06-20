def main():
    infile = open("Presidents.txt", "r")
    print("(1) Using read(): ")
    print(infile.read())
    infile.close()

    infile = open("Presidents.txt", "r")
    print("\n(2) Using read(number): ")
    s1 = infile.read(4)  #读取4个字符
    print(s1)
    s2 = infile.read(10)  #读取10个字符
    print(repr(s2))
    infile.close()

    infile = open("Presidents.txt", "r")
    print("\n(3) Using readline(): ")
    line1 = infile.readline()  #readline()方法读取下一行，以读取\n结束的一行
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()
    print(repr(line1))
    print(repr(line2))
    print(repr(line3))
    print(repr(line4))
    infile.close()

    infile = open("Presidents.txt", "r")
    print("\n(4) Using readlines(): ")
    print(infile.readlines())  #readlines()方法读取所有行并放入一个字符串列表中
    infile.close()

main()