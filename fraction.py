import math
def lcm(x,y):
    a=x
    b=y
    if(a<b):
        a,b=b,a
       
    while(b!=0):
        k=a % b
        a=b
        b=k
    r=(x*y) / a
    return r


class fraction:
    def __init__(self,numerator,denominator):
        self.numerator=numerator
        self.denominator=denominator
       
    
    def add(self,fraction2):
        
        if(self.denominator==fraction2.denominator):
            numerator=self.numerator+fraction2.numerator
            denominator=self.denominator
        else:

            k=lcm(self.denominator,fraction2.denominator)
            numerator=self.numerator*k+fraction2.numerator*k
            denominator=k
        result=fraction(numerator,denominator)
        result.print()

    def sub(self,fraction2):
        
        if(self.denominator==fraction2.denominator):
            numerator=self.numerator-fraction2.numerator
            denominator=self.denominator
        else:

            k=lcm(self.denominator,fraction2.denominator)
            numerator=self.numerator*k-fraction2.numerator*k
            denominator=k
        result=fraction(numerator,denominator)
        result.print() 

            

    def mul(self,fraction2):
        
        numerator=self.numerator*fraction2.numerator
        denominator=self.denominator*fraction2.denominator
        result=fraction(numerator,denominator)
        result.print()
        
    
    def div(self,fraction2):
        
        numerator=self.numerator*fraction2.denominator
        denominator=self.numerator*fraction2.denominator
        result=fraction(numerator,denominator)
        result.print()

    def print(self):
        print("Fraction=",self.numerator,"/",self.denominator)
      

fr1=fraction(2,3)
fr1.print()
fr2=fraction(3,5)
fr2.print()
#menu

choice=int(input("1.add 2.sub 3.mul 4.div :"))
if(choice==1):
    fr1.add(fr2)    
elif(choice==2):
    fr1.sub(fr2)
elif(choice==3):
    fr1.mul(fr2)
elif(choice==4):
    fr1.div(fr2)
else:
    print("something went wrong")


    
    



        
