# Qno1
# class Vehicle:
#    def __init__(self,brand,model):
#       self.brand = brand
#       self.model = model
#    def show_detail(self):
#       return f"Brand: {self.brand} Model: {self.model}"

# class Motercycle(Vehicle):
#    def __init__(self, brand, model,has_sidecar):
#       super().__init__(brand, model)
#       self.has_sidecar = has_sidecar

# motercycle = Motercycle("Honda",2023,"bike")
# detail = motercycle.show_detail()
# print(f"{detail} {motercycle.has_sidecar}")

# Qno2
# class Person:
#    def __init__(self,name,age,gender):
#       self.name = name
#       self.age = age
#       self.gender = gender
   
# class Employee:
#    def __init__(self,empId,post):
#       self.empId = empId
#       self.post = post

# class Developer(Person,Employee):
#    def __init__(self, name, age, gender,empId,post,programming_languge):
#       Person.__init__(self,name, age, gender)
#       Employee.__init__(self,empId,post)
#       self.programming_language = programming_languge

#    def show_detail(self):
#       print(f"Name: {self.name} Age: {self.age} Geder: {self.gender} ")
#       print(f"Employee Id: {self.empId} Post: {self.post}\nProgramming Language: {self.programming_language}")

# devloper = Developer("Abu Hurera",23,"Male",5321,"Java Developer","Java")
# devloper.show_detail()

# Qno3
# class Animal:
#    def __init__(self):
#       pass
#    def eat(self):
#       print("Eating.....")

# class Bird(Animal):
#    def __init__(self):
#       super().__init__()
#    def eat(self):
#       print("Birds are Eating........")
#    def fly(self):
#       print("Birds Are Flying")

# bird = Bird()
# bird.eat()
# bird.fly()

Qno4
