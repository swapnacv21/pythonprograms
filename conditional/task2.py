# if elif ladder:

# a=int(input("enter the first number"))
# b=int(input("enter the second number"))
# if a>b:
#     print('a is greater')
# elif a==b:
#     print('a and b are equal')
# else:
#     print("b is greater")

# nested if:

a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=int(input('enter 3rd number'))
if a>b:
    if a>c:
        print("a is large")
    else:
        print("c is large")
else:
    if b>c:
        print("b is large")
    else:
        print("c is large")