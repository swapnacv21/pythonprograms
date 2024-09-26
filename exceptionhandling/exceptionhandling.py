'''EXCEPTION HANDLING'''
# ---------------------------

'''
--->used to handle error
---> keywords used:
1)try
2)except
3)else
4)finally
'''

# example:
# -------------

'''print('welcome')
a='welcome'
b=20
print(a+b)'''     #---------> error

'''handling this error using try keyword:'''
# ---------------------------------------------

# print('welcome')
# a='welcome'
# b=20
# try:
#     print(a+b)
# except:
#     print('an error')

'''OUTPUT:'''
# welcome
# an error
    

'''else and finally keyword:'''
# ---------------------------------


# print('welcome')
# a='welcome'
# b=20
# try:
#     print(a+b)
# except:
#     print('an error')
# else:       #-------------> works only when there is no error
#     print("else") 
# finally:    #-------------> works evenif there is error or not
#     print("program ends")
# print("sample print")

'''OUTPUT:'''

# welcome
# an error
# program ends
# sample print



'''Example 1: using exception handling in a program'''
# --------------------------------------------------------

# while True:
#     print(
#         '''
#         1.Add
#         2.Sub
#         3.Exit
#         '''
#     )
#     while True:
#         try:
#             choice=int(input("Enter your choice :"))
#             break
#         except:
#             print("incorrect data. Enter choice again")
#     if choice==1:
#         print("Addition")
#     elif choice==2:
#         print("Subtraction")
#     elif choice==3:
#         break

'''Example 2: sum of numbers in a list'''
# --------------------------------------------

# l=[1,2,3,4,5.8,'abc']
# s=0
# for i in l:
#     try:
#         s+=i
#     except:
#         pass
# print(s)

# OUTPUT: 15.8

'''sum of numbers in a list without using exception handling:'''
# ---------------------------------------------------------

l=[1,2,3,4,5.8,'abc']
s=0
for i in l:
    print(type(i))
    if type(i)==int or type(i)==float:
        s+=i
print(s)

# output: 15.8