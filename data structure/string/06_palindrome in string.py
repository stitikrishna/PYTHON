string="mom"

if string==string[::-1]:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")
    
    
#another way
rev_str=""
for i in range(len(string)-1,-1,-1):
    rev_str +=string[i]
#print(rev_str)    
if string==rev_str:
    print(f"{string} is palindrome")
else:
    print(f"{string} is not a palindrome")            