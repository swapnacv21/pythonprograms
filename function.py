'''Function
----------------'''

# def fun1():              #creating a var using def keyword
#     print("hai")
#     print("welcome")
#     print("python")
#     print("php")

# print(10+2)
# fun1()                   #calling a function
# print(10-5)
# fun1()
# print(10/5)
# fun1()

'''output:
12
hai
welcome
python
php
5
hai
welcome
python
php
2.0
hai
welcome
python
php'''


# Scope of a Variable
# -----------------------

'''def fun1():
    a=10          #local variable :  scope - only inside the function
    print("a=",a)
    print("b inside=",b)

b=50              #global variable : scope - all over the program
print("b outside=",b)
fun1()'''

# output:

# b outside= 50
# a= 10
# b inside= 50

# How to create a  global variable inside a function:
'''(coverts a variable into global variable using  the keyword global)'''

# def fun():
#     global a
#     a=20
#     print("global a =",a)
# b=10
# print("outside b=",b)
# fun()

# output:

# outside b= 10
# global a = 20



'''return - to return values from a function '''
# ----------------------------------------------

'''def fun():
    return 'welcome',20,'hello' '''

#( print(fun())              #output:('welcome', 20, 'hello') )

'''a,b,c=fun()
print(a)
print(b)
print(c)'''

# output:
# welcome
# 20
# hello

# -------------------------------------------------------------------------------------

""" * local variables can be accessed outside a function using return keyword"""
# example:

'''def fun():
    a=5
    b=10
    c=15
    return a,b,c
x,y,z=fun()
print("a = ",x)
print("b = ",y)
print("c = ",z)'''

# output:
# a =  5
# b =  10
# c =  15

