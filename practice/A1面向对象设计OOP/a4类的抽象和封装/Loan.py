# -*- coding:utf-8 -*-
class Loan:
    def __init__(self, annualInterestRate = 2.5,
                 numberOfYears = 1, loanAmount = 1000, borrower = 'wang'):

       self.__annualInterestRate = annualInterestRate
       self.__numberOfYears = numberOfYears
       self.__loanAmount = loanAmount
       self.__borrower = borrower

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def getNumberOfYears(self):
        return self.__numberOfYears

    def getLoanAmount(self):
        return self.__loanAmount

    def getBorrower(self):
        return self.__borrower

    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate

    def setNumberOfYears(self, numberOfYears):
        self.__numberOfYears = numberOfYears

    def setLoanAmount(self, loanAmount):
        self.__loanAmount = loanAmount

    def setBorrower(self, borrower):
        self.__borrower = borrower

    def getMonthlyPayment(self):
        monthlyInterestRate = self.__annualInterestRate / 1200
        monthlyPayment = self.__loanAmount * monthlyInterestRate / (1 - (1 / (1 + monthlyInterestRate) ** (self.__numberOfYears *12)))
        return monthlyPayment

    def getTotalPayment(self):
        totalPayment = self.getMonthlyPayment() * self.__numberOfYears * 12
        return totalPayment


if __name__ == '__main__':
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
