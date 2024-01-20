# class Hello:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def hello(self):
#         print("Hello, World!")

#     def sum(self, x):
#         return (x+1)

#     def dummy(self):
#         print("dummy")    

#     def get_name_age(self):
#         print(self.name, self.age)

#     def dif_age(self, age):
#         print(self.name)
#         self.age = age
#         print(self.age)    


# # f =Hello("cahar", 35)
# # f.get_name_age()
# # f.dif_age(56)
# f = Hello("caharn", 46)
# print(f)
#####################////////////////////////////////////////////////////////////////////////////////////////
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade    

class Course:
    def __init__(self, name, max_std):
        self.name = name
        self.max_std = max_std
        self.Students = []

    def add_std(self, student):
         if len(self.Students) < self.max_std:
            self.Students.append(student)  
            return True
         return False

    def get_avg(self):
        value = 0
        for student in self.Students:
            value += student.get_grade()

        return value/len(self.Students)    


s1 = Student("charan", 19, 10)
s2 = Student("das", 17, 200)
s3 = Student("sai", 18, 90)

course = Course("math", 5)
course.add_std(s1)
course.add_std(s2)
course.add_std(s3)

print(course.get_avg())
