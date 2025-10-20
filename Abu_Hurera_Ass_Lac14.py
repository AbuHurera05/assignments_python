# Qno1
# FILE_PATH="input.txt"
# COUNT_TXT_PATH="count.txt"
# try:
#    file = open(FILE_PATH,'r')
#    line = file.readlines()
#    count=0
#    for i in line:
#       print(i,end="")
#       count+=1
#    file.close
#    count=str(count)
#    file = open(COUNT_TXT_PATH,'w')
#    count_text = file.write("Row in input.txt is: "+count)
# except FileNotFoundError:
#    print("File not found")

# Qno2
# FILE_PATH="input.txt"
# COUNT_TXT_PATH="count.txt"
# try:
#    with open(FILE_PATH,'r') as file:
#       line = file.readlines()
#       count=0
#       for i in line:
#          print(i,end="")
#          count+=1
#    file.close
#    count=str(count)
#    with open(COUNT_TXT_PATH,'w') as file:
#       count_text = file.write("Row in input.txt is: "+count)
# except FileNotFoundError:
#    print("File not found")

# Qno3
import csv
FILE_PATH = "data.csv"
FILE_PATH1 = 'data1.csv'
try:
   with open(FILE_PATH,'w') as fileWrite:
      with open(FILE_PATH1,'r') as fileRead:
         rows = csv.DictReader(fileRead)
         for row in rows:
            if row['Age'] > str(25):
               csv.DictWriter(fileWrite)
               print(row)
except FileNotFoundError:
   print("File Not Found")
