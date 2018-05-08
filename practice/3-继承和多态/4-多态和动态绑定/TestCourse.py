# -*- coding:utf-8 -*-
'''
类之间的常见关系有关联、聚合、继承。
关联举例：一个学生可以选修任意多门课程，一名教员最多可以教授三门课，一门课最多可以有5-60名学生，且只能由一名教员。
聚合举例：一名学生有一个名字，是Student类和Name类的一种组合关系，但是，一名学生有一个地址，是Student类和Address类
的一种聚合关系，因为一个地址可以被多个学生所共用。
因为聚合只是关联的一种特殊形式，并且在类中使用同样的方法实现，为了简化，统称为组合
'''
from Course import Course

def main():
    course1 = Course("数学")
    course2 = Course("语文")

    course1.addStudent("zhao")
    course1.addStudent("qian")
    course1.addStudent("sun")

    course2.addStudent("li")
    course2.addStudent("zhou")

    print("Number of students in course1:", course1.getNumberOfStudents())
    students = course1.getStudents()
    for student in students:
        print(student, end = ", ")  #每个名字字符串结尾处添加逗号

    print("\nNumber of students in course2:", course2.getNumberOfStudents())

main()