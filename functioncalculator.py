# program: basic calculator

def numbers():
    a=int(input("Enter 1st number"))
    b=int(input("Enter 2nd number"))
    return a,b
def add():
    a,b=numbers()
    print(a+b)
def sub():
    a,b=numbers()
    print(a-b)
def mul():
    a,b=numbers()
    print(a*b)
def div():
    a,b=numbers()
    print(a/b)
def mod():
    a,b=numbers()
    print(a%b)
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
        add()
    elif choice==2:
        sub()
    elif choice==3:
        mul()
    elif choice==4:
        div()
    elif choice==5:
        mod()
    elif choice==6:
        break

    # ---------------------------