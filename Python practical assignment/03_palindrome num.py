number=(input("enter a number"))

revstr=""

for i in number:
    revstr= i+revstr
    print("Reverse number:",revstr)
    
    
if(number == revstr) :
     print("number is palidrome")
     
else:
    print("number is not palindrome ")     
    
    
