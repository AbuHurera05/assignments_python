# ______________________________Dictionary________________________
# Qno1
# car = {"brand":"civic","model":2020,"year":2020,"price":5000000}
# for i in car.values():
#    print(i)

# Qno2
# car["color"] = "Red"
# car["price"] = 55000000
# print(car)

# Qno3
# car.pop("year")
# print(car)

# Qno4: ??
# text = "apple banana apple"
# lis = text.split(" ")
# dic = {}
# print(dic)
# print(lis)
# for i in lis:
#    dic[dic.setdefault(i,1)+1]=i
# # print(dic)
# print(dic.items())

# Qno5
# student = {"Ali":85,"Sara":92,"Ahmad":78}
# small=0
# newKey = 0
# for i in student.keys():
#    if student.get(i) > small:
#       small = student.get(i)
#       newKey = i
# print(f"{newKey} : {student.get(newKey)}")

# Qno6
# dic1 = {"a":1,"b":2}
# dic2 = {"c":3,"d":4}
# dic1.update(dic2)
# print(dic1)

# _________________________________Set__________________________
# Qno1
# set1 = {"banana","apple","banana","apple","cherries"}
# print(set1)

# Qno2
# print("apple" in set1)

# Qno3
# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
# common = a.intersection(b)
# print(common)

# Qno4
# unique = a.difference(b)
# print(unique)

# QNo5
# allUnique = a.symmetric_difference(b)
# print(allUnique)

# Qno6
# list = [1,2,3,4,1,1,2,5,5,4,9,10]
# print(list)
# set2 = set(list)
# print(set2)
