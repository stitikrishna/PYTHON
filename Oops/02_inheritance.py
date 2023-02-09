class Mathclass:
    
    def sum(self,a,b):
        return a+b
    
    def sub(self,a,b):
        return a-b
    
    def mul(self,a,b):
        return a*b
    
    def div(self,a,b):
        return a/b
    
    def mod(self,a,b):
        return a%b





class Expression(Mathclass):
    
    def lhs(self,a,b)    :
        return self.mul(
            self.sum(a,b),
            self.sum(a,b)
        )
    def rhs(self,a,b)    :
        return self.sum(
          self.sum(
              self.mul(a,a),
              self.mul(b,b)
              )  ,
           self.sum(
              self.mul(a,b),
              self.mul(a,b)
              )  
        )    
      
     
        
    
obj=Expression()
print(obj.lhs(2,3))
print(obj.rhs(2,3))
    
obj=Mathclass()
print(obj.mod(2,3))    
print(obj.sum(2,3))  
print(obj.sub(2,3))  
print(obj.div(2,3))  
print(obj.mul(2,3))     
     