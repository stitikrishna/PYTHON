student={
    1:{
        "name":"barsha",
        "age":20,
        "university":"NIT",
        "grade": {
            "10th":90,
            "12th":80,
            "be":85
        }
            
    },
    2:{
        "name":"puja",
        "age":20,
        "university":"NIT",
        "grade":{
            "10th":90,
            "12th":80,
            "be":85
        }
            
    }  

}


for i in student.keys():
    for j in student[i].keys():
        print(j,student[i][j])
    print()     