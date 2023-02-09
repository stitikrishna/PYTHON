def linearSearch(mylist,val):
    for i in mylist:
        if i==val:
            return True
    return False


mylist=[1,2,3,4,5,1]

print(linearSearch(mylist,5))   
    
#print(mylist.count(1))
#mylist.sorts(reverse=True)
#print(mylist)