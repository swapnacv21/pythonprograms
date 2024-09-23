import numbers
import add as z
import sub as x
from mul import mul
from div import div
from mod import *
while True:
    print(
        '''
        1.Addition
        2.Subtraction
        3.Multiplication
        4.Division
        5.Modulus
        6.Exit
        '''
    )        
    choice=int(input("Enter your choice : "))
    if choice==1:
        a,b=numbers.num()
        z.add(a,b)
    elif choice==2:
        a,b=numbers.num()
        x.sub(a,b)
    elif choice==3:
        a,b=numbers.num()
        mul(a,b)
    elif choice==4:
        a,b=numbers.num()
        div(a,b)
    elif choice==5:
        a,b=numbers.num()
        mod(a,b)
    elif choice==6:
        break
