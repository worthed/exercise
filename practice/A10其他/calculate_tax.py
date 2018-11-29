# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/19 下午6:29
IDE：PyCharm
描述：
"""
import sys
import bisect

def old_tax(salary):
    if salary < 3500:
        return 0.0

    above = salary - 3500

    ranges = [0, 1500, 4500, 9000, 35000, 55000, 80000]
    rate =   [.03, .1,  .2,  .25,  .30,   .35,   .45]
    i = bisect.bisect_left(ranges, above)
    j = 0
    tax = 0.0
    while j < i:
        if j+1 < i:
            tax += (ranges[j+1]-ranges[j]) * rate[j]
        else:
            tax += (above-ranges[j]) * rate[j]
        j += 1

    return tax


def new_tax(salary):
    if salary < 5000:
        return 0.0

    above = salary - 5000

    ranges = [0, 1500, 4500, 9000, 35000, 55000, 80000]
    rate =   [.03, .1,  .2,  .25,  .30,   .35,   .45]
    i = bisect.bisect_left(ranges, above)
    j = 0
    tax = 0.0
    while j < i:
        if j+1 < i:
            tax += (ranges[j+1]-ranges[j]) * rate[j]
        else:
            tax += (above-ranges[j]) * rate[j]
        j += 1

    return tax

if __name__ == "__main__":
    '''
    if len(sys.argv) < 2:
        print("Usage: {} <salary>".format(sys.argv[0]))
        sys.exit(1)

    salary = float(sys.argv[1])
    '''
    salary = float(8999)
    old_tax = old_tax(salary)
    new_tax = new_tax(salary)
    print("old: {}, new: {}".format(old_tax, new_tax))
