# operators:

# 1)Arithmetic Operators:

# addition:
print(10+5)
print('Jibin'+'Aji')

# subtraction:
print(10-5)

# multiplication:
print(10*5)
print('python'*2)

# division:
print(10/2)

# modulus:
print(10%5)

# floor division:
print(10//5)
print(10//3)

# exponent:
print(10**3)
print(10**2)

# 2)Assignment Operators:

# =
a=10
print(a)

# +=
a=10
a+=5
print(a)

# -=
a=10
a-=5
print(a)

# *=
a=10
a*=5
print(a)

# /=
a=10
a/=5
print(a)

# %=
a=10
a%=5
print(a)

# //=
a=10
a//=3
print(a)

# **=
a=10
a**=2
print(a)

# 3)Comparison Operators:

# ==
print(10==10)
print(10==2)

# !=
print(10!=10)
print(10!=5)

# >
print(10>9)
print(10>11)

# <
print(10<9)
print(10<15)

# >=
print(10>=10)
print(10>=5)
print(10>=16)

# <=
print(10<=10)
print(10<=8)
print(10<=20)

# 4)Logical Operators:

# and:
print(10==10 and 5==5)
print(10==10 and 10==5)
print(10>12 and 10<12)
print(10>20 and 10>30)

# or:
print(20==20 or 10==10)
print(20==20 or 20==10)
print(10<15 or 10==10)
print(20==10 or 20==90)

# not:
print(not(10==10))
print(not(10==11))

# 5)Membership Operators:

# in:
print('e' in 'welcome')
print('a' in 'welcome')
list=[10,20,30]
print(10 in list)
list=[10,20,30]
print(60 in list)

# not in:
print('e' not in 'welcome')
print('i' not in 'welcome')
list=[10,20,30]
print(10 not in list)
list=[10,20,30]
print(60 not in list)

# 6)Identity Operators:
# is:
a=10
b=10
print(a is b)
print(id(a))
print(id(b))

a=5
b=10
print(a is b)
print(id(a))
print(id(b))

list=[10,20,30]
list1=[10,20,30]
print(list is list1)
print(id(list))
print(id(list1))

# is not:
a=10
b=10
print(a is not b)

a=10
b=5
print(a is not b)

list=[11,12,13]
list1=[11,12,13]
print(list is not list1)