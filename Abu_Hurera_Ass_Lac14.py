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

FILE_PATH="input.txt"
COUNT_TXT_PATH="count.txt"
try:
   with open(FILE_PATH,'r') as file:
      line = file.readlines()
      count=0
      for i in line:
         print(i,end="")
         count+=1
   file.close
   count=str(count)
   with open(COUNT_TXT_PATH,'w') as file:
      count_text = file.write("Row in input.txt is: "+count)
except FileNotFoundError:
   print("File not found")