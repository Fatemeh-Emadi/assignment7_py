import math
class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def show(self):
        print(self.real,"+",self.img,"i")
    
    def add(self,complex2):
       
       real=self.real+complex2.real
       img=self.img+complex2.img
       result = complex(real,img)
       result.show()
        

    def sub(self,complex2):
        
        real=self.real-complex2.real
        img=self.img-complex2.img
        result = complex(real,img)
        result.show()

    
    def mul(self, complex2):
        
        real = self.real * complex2.real + self.img * -complex2.img
        img = self.real * complex2.img + self.img * complex2.real
        result = complex(real,img)
        result.show()
        
cmp1=complex(3,5)
cmp1.show()
cmp2=complex(2,3)
cmp2.show()
choice=int(input("1.add 2.sub 3.mul:"))
if(choice==1):
   cmp1.add(cmp2) 
      
elif(choice==2):
    cmp1.sub(cmp2)
elif(choice==3):
    cmp1.mul(cmp2)
else:
    print("something went wrong") 
        
