# program: basic calculator

while True:
    print('''
1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Modulus
6.Floordivision
7.Exponent
8.Exit''')
    choice=int(input("enter your choice"))
    if choice==1:
        a=int(input("Enter 1st number"))
        b=int(input("Enter 2nd number"))
        print(a+b)
    elif choice==2:
        a=int(input("Enter 1st number"))
        b=int(input("Enter 2nd number"))
        print(a-b)
    elif choice==3:
        a=int(input("Enter 1st number"))
        b=int(input("Enter 2nd number"))
        print(a*b)
    elif choice==4:
        a=int(input("Enter 1st number"))
        b=int(input("Enter 2nd number"))
        print(a/b)
    elif choice==5:
        a=int(input("Enter 1st number"))
        b=int(input("Enter 2nd number"))
        print(a%b)
    elif choice==6:
        a=int(input("Enter 1st number"))
        b=int(input("Enter 2nd number"))
        print(a//b)
    elif choice==7:
        a=int(input("Enter 1st number"))
        b=int(input("Enter 2nd number"))
        print(a**b)
    elif choice==8:
        break