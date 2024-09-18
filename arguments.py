# Types of arguments:
'''----------------------'''


# 1) Positional Argumnets (no of parameters = no of arguments)
'''---------------------------------'''

'''example:'''

# def dtls(name,age):            ----> parameters -  used to collect values, given when creating a function
#     print('name= ',name)
#     print('age= ',age)
# dtls('jibin',21)               ----> arguments - given when calling function
# dtls('swapna',20)
# dtls(26,'sandra')

'''output:

name=  jibin
age=  21
name=  swapna
age=  20
name=  26
age=  sandra'''


# 2)Keyword arguments (variables are used in argument)
'''-------------------'''

'''example:'''

# def dtls(name,age):
#     print("name = ",name)
#     print("age = ",age)
# dtls(age=22,name='alex')


''' output:

name =  alex
age =  22'''

# 3) Default arguments ()
'''-------------------------'''

'''example : '''

# def sample(name='abcd',age=29):
#     print(name,age)
# sample('manu')
# sample('akshay',25)
# sample(age=28)

'''output:
manu 29
akshay 25
abcd 28'''

# 4) Arbitary arguments ()
'''----------------------'''

'''example : '''


# def sample(b,*a):
#     print(b,a)

# sample(20)
# sample(1,2,3)
# sample(1,2,3,4)

'''output: 
20 ()
1 (2, 3)
1 (2, 3, 4)'''


# 5) Arbitory keyword Arguments ()
'''----------------------------'''

'''example : '''

# def sample(**a):
#     print(a)

# sample(name='sonu',age=23)
# sample(name='rithu',age=20,name1='veena',age1=26)

'''output:
{'name': 'sonu', 'age': 23}
{'name': 'rithu', 'age': 20, 'name1': 'veena', 'age1': 26}'''