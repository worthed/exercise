# -*- coding:utf-8 -*-
UML类图
BMI
#数据域    - 表示私有数据域
__name: str
__age: int
__weight: float
__height: float

BMI(name: str,
age: int,
weight: float,
height: float)  #构建一个有指定姓名、年龄（默认为20）、体重和身高的BMI对象

getBMI(): float  #返回BMI
getStatus(): str #返回BMI状态（例如：正常、超重等）