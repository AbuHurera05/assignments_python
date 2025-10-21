# Qno 1
name= "Ali"
age = 20
grade = 'A'
school_Name="Raheem Public School Badin"
print(f"My name is {name}, I am {age} years old, I Study in class {school_Name}.")

# Qno2 
name = input("Enter your name:")
age = input("Enter your Age:")
height = input("Enter your Height:")
print(f"Your name is {name}, you are {age} yers old,and your height is {height} meters")

# Qno3
num1 = input("Enter number1:")
num2 = input("Enter number2:")
num1 = int(num1)
num2 = int(num2)
print(f"Sum: {num1+num2}")
print(f"Difference: {num1-num2}")
print(f"Product: {num1*num2}")
print(f"Quotient: {num1/num2}")

# Qno4
score=0
score=score+10
score=score+10
score=score+10
print(score)

#______________Final Assignmet_______________
# Qno1
name = input("Enter your name:")
age = input("Enter your Age:")
sub1 = int(input("Enter subject1 marks:"))
sub2 = int(input("Enter subject2 marks:"))
sub3 = int(input("Enter subject3 marks:"))

total_marks = sub1+sub2+sub3
average = total_marks/3
total_marks +=5
average= total_marks/3
result="Fail"
if (average >= 40):
   result="Pass"
print(f"Student name: {name}")
print(f"Age: {age}")
print(f"Total Marks: {total_marks}")
print(f"Result: {result}")
