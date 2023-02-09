n=int(input())

if(n%3==0 and n%5==0):
    print("both are divisible by 3 and 5")
elif(n%3==0):
    print("divisible by 3")
    
elif(n%5==0):
    print("divisible by 5")
else:
    print("not divisible by 3 and 5 ")     
    