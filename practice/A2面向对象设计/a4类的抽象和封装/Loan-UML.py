# -*- coding:utf-8 -*-
UML类图
Loan
#数据域    - 表示私有数据域
__annualInterestRate: float  #贷款年利率（默认值为2.5）
__numberOfYears: int  #贷款年数（默认值为1）
__loanAmount: float  #贷款额（默认为1000）
__borrower: str  #本笔贷款的借贷者（默认为““）

Loan(annualInterestRate:float,
numberOfYears:int,
loanAmount:float,
borrower:str)  #构建一个有指定年利率、年数、贷款额和借贷者的Loan对象

getAnnualInterestRate(): float  #返回这笔贷款的年利率
getNumberOfYears(): int  #返回这笔贷款的年数
getLoanAmount(): float  #返回这笔贷款的贷款额
getBorrower(): str  #返回这笔贷款的借贷者

setAnnualInterestRate(annualInterestRate:float): None  #设置这笔贷款的新的年利率
setNumberOfYears(numberOfYears:int): None  #设置这笔贷款的新的年数
setLoanAmount(loanAmount:float): None  #设置这笔贷款的新的贷款额
setBorrower(borrower:str): None  #设置这笔贷款的新的借贷者

getMonthlyPayment(): float  #返回这笔贷款的月支付额
getTotalPayment(): float  #返回这笔贷款的总支付额