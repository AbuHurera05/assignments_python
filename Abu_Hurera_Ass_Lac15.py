import json,csv
# Part A
# student = [
#    {"Name":"Abu Hurer","Age":23,"Marks":68},
#    {"Name":"Ahsan","Age":21,"Marks":88},
#    {"Name":"Ali Raza","Age":20,"Marks":69},
#    {"Name":"Muhammad","Age":19,"Marks":95},
#    {"Name":"Arsalan","Age":27,"Marks":60}
# ]
# with open("student.json","w") as file:
#    json_string = json.dump(student,file,indent=4)

# with open("student.json","r") as file:
#    data = json.load(file)

# for student in data:
#    if student['Marks'] <70:
#       print(student)
# print("+++++++++++++++++++++_______________+++++++++++++++++++++")

# json_string = json.dumps(data)
# print(json_string)

# Part B
# total_value = 0
# with open("products.csv","r") as file:
#    data = csv.DictReader(file)
#    for row in data:
#       price = float(row["Price"])
#       quantity = int(row["Quantity"])
#       total_value += price*quantity
#       if price > 500:
#          print(row)

# with open("products.csv","a",newline="") as file:
#    writer = csv.writer(file)
#    writer.writerow([5,"Printer",600,4])

# Part C
# with open("users.csv","w",newline="") as file:
#    writer = csv.writer(file)
#    writer.writerow(["name","email","age"])
#    writer.writerow(["Ali","ali@gmail.com",22])
#    writer.writerow(["Aslam","aslam@gmail.com",20])
#    writer.writerow(["Sarwar","sarwar@gmail.com",21])

# filter_users = []
# with open("users.csv","r") as file:
#    data = csv.DictReader(file)
#    for row in data:
#       if int(row["age"]) > 18:
#          filter_users.append(row)

# with open("users.json","w") as json_file:
#    json.dump(filter_users,json_file,indent=4)

# with open("users.json","r") as json_file:
#    data = json.load(json_file)
#    print(data)
   