from Max import max
'''
from Max import max   从Max.py中调用max函数

也可以写成 import Max , 但调用函数得为Max.max() 
'''
def main():
    i = 5
    j = 2
    k = max(i,j)
    print("数字", i, "和", j, "的最大值是", k)

main()