# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def speak(self):
#         print("bow")

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def speak(self):
#         print("meow") 
#//////////////////////////////////////////////////////////////////////////////////////////////
# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show(self):
#         print(f"iam with {self.name} name and of {self.age} age")    

#     def speak(self):
#         print("pet")


# class Dog(Pet):
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color

#     def speak(self):
#         print("bow")


# class Cat(Pet):
#     def speak(self):
#         print("meow")

# p1 = Pet("barry", 23)
# p1.speak()

# c1 = Cat("darla", 14)   
# c1.speak()

# d1 = Dog("bunny", 12, "white")
# print(d1.color)
# d1.speak()
#//////////////////////////////////////////////////////////////
# class Person:
#     no_of_pep = 0

#     def __init__(self , name, age):
#         self.name = name
#         self.age = age
#         Person.add_per()

#     @classmethod
#     def get_total_people(cls):
#         return cls.no_of_pep

#     @classmethod
#     def add_per(cls):
#         cls.no_of_pep += 1    


# p1 = Person("das" , 20)
# print(Person.get_total_people())
# p2 = Person("sai", 18)
# print(Person.get_total_people())
#/////////////////////////////////////////////////////static
class Math:
    @staticmethod
    def add1(x, y):
        return x+y

    def add2():
        pass


print(Math.add1(2,3))