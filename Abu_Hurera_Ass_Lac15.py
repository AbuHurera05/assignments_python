import json
student = [
   {"Name":"Abu Hurer","Age":23,"Marks":68},
   {"Name":"Ahsan","Age":21,"Marks":88},
   {"Name":"Ali Raza","Age":20,"Marks":69},
   {"Name":"Muhammad","Age":19,"Marks":95},
   {"Name":"Arsalan","Age":27,"Marks":60}
]
with open("student.json","w") as file:
   json_string = json.dump(student,file,indent=4)
