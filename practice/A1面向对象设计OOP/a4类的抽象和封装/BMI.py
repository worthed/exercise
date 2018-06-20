# -*- coding:utf-8 -*-
class BMI:
    def __init__(self, name, age, weight, height):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height

    def getBMI(self):
        KILOGRAMS_PER_POUND = 0.45359237
        METERS_PER_INCH = 0.0254
        bmi = self.__weight * KILOGRAMS_PER_POUND / ((self.__height * METERS_PER_INCH) * (self.__height * METERS_PER_INCH))
        return round(bmi * 100) / 100

    def getStatus(self):
        bmi = self.getBMI()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 < bmi < 25:
            return "Normal"
        elif 25 < bmi < 30:
            return "Overweight"
        else:
            return "Obese" #肥胖

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getWeight(self):
        return self.__weight

    def getHeight(self):
        return self.__height


if __name__ == '__main__':
    bmi1 = BMI("wang", 18, 145, 70)
    print("The BMI for", bmi1.getName(), "is", bmi1.getBMI(), bmi1.getStatus())

    bmi2 = BMI("li", 50, 215, 70)
    print("The BMI for", bmi2.getName(), "is", bmi2.getBMI(), bmi2.getStatus())