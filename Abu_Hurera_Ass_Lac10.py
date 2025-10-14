# Qno1
# class Book:
#    def __init__(self,title,auther):
#       self.title = title
#       self.auther = auther

#    def show_detail(self):
#       print(f"This {self.title} book is written by {self.auther}")

# book = Book("English","Arlslan")
# book.show_detail()

# Qno2
# import math as m
# class Circle:
#    def __init__(self,radius):
#       self.radius = radius

#    def area(self):
#       print(f"Area of radius: {self.radius} is {m.pi*self.radius**2}")
   
#    def circumference(self):
#       print(f"Circumference of radius: {self.radius} is {2*m.pi*self.radius}")


# circle = Circle(66)
# circle.area()
# circle.circumference()
# Qno3
# class Employee:
#    def __init__(self,name,salary):
#       self.name = name
#       self.salary = salary
   
#    def increase_salary(self,percentage):
#       self.salary = self.salary * (percentage / 100)
#       print(f"New salary of after {percentage}% increase is: {self.salary}")

# emp = Employee("Ali",20000)
# emp.increase_salary(30)

# Qno4
# class Calculator:
#    def __init__(self,num1,num2):
#       self.num1 = num1
#       self.num2 = num2
   
#    def add(self):
#       print(f"Additon: {self.num1+self.num2}")
#    def subtraction(self):
#       print(f"Subtraction: {self.num1-self.num2}")
#    def multiplication(self):
#       print(f"Multiplication: {self.num1*self.num2}")
#    def division(self):
#       if self.num2 ==0:
#          print("Error! Zero Division Error")
#       else:
#          print(f"Division: {self.num1//self.num2}")

# calc = Calculator(34,10)
# calc.add()
# calc.subtraction()
# calc.multiplication()
# calc.division()

# Qno5
# class Student:
#    def __init__(self,name,marks):
#       self.name = name
#       self.marks = marks
#    def disply_result(self):
#       if self.marks >= 50:
#          print(f"Congratulation! {self.name}, You are pass")
#       else:
#          print(f"{self.name}, You are fail")

# std = Student("Ahmad",49)
# std.disply_result()