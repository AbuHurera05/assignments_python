# Qno1
# class Employess:
#    def __init__(self,name,salary):
#       self.name = name
#       self.salary = salary
#       print(f"Name: {self.name} Salary: {self.salary}")

#    def disply_detail(self):
#       print(f"Name: {self.name} Salary: {self.salary}")
   
# emp = Employess("Abu Hurera",550000)
# emp.disply_detail()

# Qno2
# class Employess:
#    name = "Ahmad"
#    def __init__(self,name):
#       self.name = name
#    @classmethod
#    def disply_detail(cls):
#       print(f"Name: {cls.name} ")
   
# emp = Employess("Aslam")
# emp.disply_detail()

# Qno3
# class Math:
#    @staticmethod
#    def is_prime_num(num):
#       if num < 2:
#          return False
#       for i in range(2,int(num**0.5)+1):
#          if num % i ==0:
#             return False
#          return True

# math = Math()
# print(math.is_prime_num(6))

# Qno4
# class Account:
#    def __init__(self,balance):
#       self._balance = balance
#    @property
#    def get_balance(self):
#       return self._balance
#    @get_balance.setter
#    def set_balacne(self,balance):
#       self._balance = balance

# acc = Account(2000)
# print(acc.get_balance)
# acc.set_balacne=10000
# print(acc.get_balance)

# Qno5
# class Book:
#    def __init__(self,title,author,price):
#       self.title = title
#       self.author = author
#       self.price = price
   
#    def show_detail(self):
#       print(f"The {self.title} is written by: {self.author} cost: {self.price}Rs")

# book1 = Book("Java","James Goslin",2000)
# book2 = Book("Python","Guido Van Rossum",1030)
# book3 = Book("C++","Bjarne Stroustrup",800)
# book1.show_detail()
# book2.show_detail()
# book3.show_detail()