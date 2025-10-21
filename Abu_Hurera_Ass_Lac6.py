# Qno1
# try:
#    title = open("data.txt","r")
#    content = title.read()
#    print(content)
# except FileNotFoundError:
#    print("Invalid File")
# except PermissionError:
#    print("You have can not access this file")

# Qno2
# def check_num(num):
#    try:
#       if num < 0:
#          raise Exception("Number must be posivtive.")
#    except Exception as e:
#       print(e)

# check_num(-4)

# QNo3
# num1 = 5
# num2 = 0
# try:
#    print(num1//num2)
# except ZeroDivisionError as e:
#    print(e)
# finally:
#    print("Thanks for Comming....")

# Qno4
while(True):
   try:
      num = int(input("Enter a number: "))
      print(f"Hey you enter a correct number: {num}")
      break
   except ValueError as e:
      print("Invalid input! please enter an integer.")

