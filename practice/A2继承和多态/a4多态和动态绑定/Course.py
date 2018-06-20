# -*- coding:utf-8 -*-
class Course:
    def __init__(self, courseName):
        self.__courseName = courseName
        self.__students = []

    def addStudent(self, student):
        self.__students.append(student)

    def getStudents(self):
        return self.__students

    def getNumberOfStudents(self):
        return len(self.__students)

    def getCourseName(self):
        return self.__courseName

    def DropStudent(self, student):
        self.__students.remove(student)


if __name__ == '__main__':
    '''
    类之间的常见关系有关联、聚合、继承。
    关联举例：一个学生可选多门课，一名教员最多可以教三门课，一门课最多有60名学生，只能有一名教员。
    聚合举例(关联的一种特殊形式)：一名学生有一个名字，是Student类和Name类的一种组合关系，但是，一名学生有一个地址，
                            但地址可被多个学生使用，故Student类和Address类是一种聚合关系
    '''
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
        print(student, end=", ")  # 每个名字字符串结尾处添加逗号

    print("\nNumber of students in course2:", course2.getNumberOfStudents())
