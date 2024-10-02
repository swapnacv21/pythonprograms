'''calculator using function:'''
# ----------------------------------

def add():
    a=int(input("Enter 1st number : "))
    b=int(input("Enter 2nd number : "))
    print(a+b)
def sub():
    a=int(input("Enter 1st number : "))
    b=int(input("Enter 2nd number : "))
    print(a-b)
def mul():
    a=int(input("Enter 1st number : "))
    b=int(input("Enter 2nd number : "))
    print(a*b)
def div():
    a=int(input("Enter 1st number : "))
    b=int(input("Enter 2nd number : "))
    print(a/b)
def mod():
    a=int(input("Enter 1st number : "))
    b=int(input("Enter 2nd number : "))
    print(a%b)
while True:
    print(
        '''
1.add
2.sub
3.mul
4.div
5.mod
6.exit
'''
    )
    choice=int(input("Enter your choice "))
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