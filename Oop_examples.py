# OOPS 

# class Employee:
#     name = "Harry"
#     language = "python"
#     salary = 1234567890

# harry = Employee()
# harry.name = "Harry"
# print(harry.name,harry.language,harry.salary)    

# rohan = Employee()
# rohan.name = "Rohan"
# print(rohan.name,rohan.language,rohan.salary)


# class Employee:
#     name = "Harry" # class Attributes
#     language = "python"
#     salary = 1234567890

# harry = Employee()
# harry.name = "Harry" #instance attributess
# harry.language = "Java"
# print(harry.name,harry.language,harry.salary)    

# #instance attributes are also priotrized above the class attributes
	
"""
class programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
            self.name = name
            self.salary = salary
            self.pin = pin
    
p = programmer("Harry", 120000, 2313231)
print(p.name, p.salary, p.pin ,p.company)
r = programmer("Rohan",120000,2313231)
print(r.name, r.salary, r.pin, r.company)
 

"""


# class calculator:
#     def __init__(self,n):
#         self.n = n
#     def square(self):
#         print(f"The square is {self.n*self.n}")
#     def cube(self):
#         print(f"The cube is{self.n*self.n*self.n}")
#     def squareroot(self):
#         print(f"The squareroot is{self.n**1/2}")
		
#     @staticmethod
#     def hello():
#          print("Hello There")

# a = calculator(4)
# a.hello()
# a.cube()
# a.squareroot()	
 
"""
class Demo:
    a = 4

o = Demo()
o.a = 0
print(o.a)
o.a = 0
print(o.a)
print(Demo.a)
"""



# from random import randint

# class Train:

#     def __init__(self,trainNo):
#         self.trainNo = trainNo


#     def book(self, fro, to):
#         print(f"Ticket is booked in train no:{self.trainNo} from {fro} to {to}") 
    
    
#     def getStatus(self):
#         print(f"Train Number : {self.trainNo} is running on Time")
    
#     def getFare(self, fro, to):
#         print(f"The fare in Train no: {self.trainNo} from {fro} to {to} is {randint(22,3467865)}")

# t = Train(1231212)
# t.book("Delhi","Mumbai")        


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def introduce(self):
#         print(f"My name is {self.name} and I am {self.age} years Old")
# s1 = Student("Akshat",20)
# s1.introduce()


"""
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

calc = Calculator()
print(calc.add(5, 3))
print(calc.subtract(10, 4))

"""


# class Animal:
#     def speak(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")

# d = Dog()
# d.speak()


# class Employee:
#     company = "TechCorp"

# def __init__(self, name, salary) :
#     self.name = name
#     self.salary = salary

# e1 = Employee("John",50000)
# e2 = Employee("Emma",100000)

# print(e1.company)
# print(e2.company)

