'''calculator using modules:'''
# -----------------------------------

import pythonprograms.practicalexam.calcmodule.nums as nums
import pythonprograms.practicalexam.calcmodule.addition as p
import pythonprograms.practicalexam.calcmodule.subt as s
import pythonprograms.practicalexam.calcmodule.mult as m
import pythonprograms.practicalexam.calcmodule.divi as d
import pythonprograms.practicalexam.calcmodule.mod as mo
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
        a,b=nums.num()
        p.add(a,b)
    elif choice==2:
        a,b=nums.num()
        s.sub(a,b)
    elif choice==3:
        a,b=nums.num()
        m.mul(a,b)
    elif choice==4:
        a,b=nums.num()
        d.div(a,b)
    elif choice==5:
        a,b=nums.num()
        mo.mod(a,b)
    elif choice==6:
        break

