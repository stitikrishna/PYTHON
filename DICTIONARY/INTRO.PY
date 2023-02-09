from pprint import pprint
student={
    0 :"no info",
    "name":"max",
    "age":21,
    "university":"ABC university",
    "grade": {
        "10th":90,
        "12th":80,
        "be":85
    }
        
        
}

for i in student.keys():
    print(i,student[i])
pprint(student)
student["branch"]="CSE"
print()
print()
pprint(student)    
grade=student["grade"]
print(grade["12th"])
print(student["grade"]["12th"])

"""
grade=student["grade"]
print(grade["be"])     
print(student["grade"]["be"])
print(student["[university"])
              
print(student.keys())
print(student["name"])


print(student[0])
for i in student.keys():
   print(i,student[i])
   """