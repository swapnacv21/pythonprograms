# Basic calculator using lambda function:
# -----------------------------------------

def numbers():
    a=int(input("Enter 1st number"))
    b=int(input("Enter 2nd number"))
    return a,b

add=lambda a,b:a+b
sub=lambda a,b:a-b
mul=lambda a,b:a*b
div=lambda a,b:a/b
mod=lambda a,b:a%b

while True:
    print('''
1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Modulus
6.Exit''')
    choice=int(input("enter your choice"))
    if choice==1:
        a,b=numbers()
        print(add(a,b))
    elif choice==2:
        a,b=numbers()
        print(sub(a,b))
    elif choice==3:
        a,b=numbers()
        print(mul(a,b))
    elif choice==4:
        a,b=numbers()
        print(div(a,b))
    elif choice==5:
        a,b=numbers()
        print(mod(a,b))
    elif choice==6:
        break



