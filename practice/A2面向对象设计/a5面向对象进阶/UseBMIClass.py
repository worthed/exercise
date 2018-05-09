# -*- coding:utf-8 -*-
from BMI import BMI

def main():
    bmi1 = BMI("wang", 18, 145, 70)
    print("The BMI for", bmi1.getName(), "is", bmi1.getBMI(), bmi1.getStatus())

    bmi2 = BMI("li", 50, 215, 70)
    print("The BMI for", bmi2.getName(), "is", bmi2.getBMI(), bmi2.getStatus())

main()