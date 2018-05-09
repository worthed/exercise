# -*- coding:utf-8 -*-
from Loan import Loan

def main():
    annualInterestRate = eval(input("输入年利率:"))

    numberOfYears = eval(input("输入贷款年数:"))

    loanAmount = eval(input("输入贷款额:"))

    borrower = (input("输入贷款人:"))

    loan = Loan(annualInterestRate, numberOfYears, loanAmount, borrower)

    print("贷款是谁的:", loan.getBorrower())
    print("每月应还:", format(loan.getMonthlyPayment(), ".2f"))
    print("总计应还:", format(loan.getTotalPayment(), ".2f"))

main()

'''
main函数
①读取利率、支付周期（以年为单位）和贷款额
②创建Loan对象
③使用Loan类的实例方法获取月支付额和总支付额
'''