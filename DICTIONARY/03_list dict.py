student=[
    {
        "name":"barsha",
        "age":20,
        "university":"NIT",
        "grade": {
            "10th":90,
            "12th":80,
            "be":85
        }
            
    },
     {
        "name":"puja",
        "age":20,
        "university":"NIT",
        "grade":{
            "10th":90,
            "12th":80,
            "be":85
        }
            
    }  

]

for i in range(len(student)): 
    for j in student[i].keys():
        print(j),
        
    print(i,student[i])    

"""
for i in range(len(student)):
    for j in student[i].keys():
         print(j,student[i][j])
    print()     
    """