n=int(input())

_sum=0
while n>0:
    rem=n%10
    _sum =_sum*10+rem
    n=int(n/10)
print(_sum)    
        
