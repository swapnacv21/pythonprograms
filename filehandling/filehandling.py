# f=open('pythonprograms/filehandling/demo.txt','a')

'''# writing a content when creating a file'''

# f.write("Hello, Welcome to all") 
# f.write('2024')

'''Read contents in a file'''

# print(f.read())
# a=f.read(5)
# f.seek(0) ------------------------> to change cursor point
# b=f.read()
# print(a)
# print('_'*20)
# print(b)

'''readline()'''

# a=f.readline(5)
# b=f.readline()
# print(a)
# print(b)


# c=f.readlines()
# print(c)

# reverse:
# -----------
# d=f.readlines()
# f.seek(0)
# for i in range(len(d)):
#     a=f.readline().strip()
#     print(a[::-1])
    # print(a)

# count letters of a string:
# ------------------

# f=open('pythonprograms/filehandling/demo.txt','r')
# e=f.readlines()
# f.seek(0)
# letter=0
# for i in range(len(e)):
#     a=f.readline().strip()
#     for i in a:
#         if i !=' ':
#             letter+=1
# print(letter)

# output: 13

'''how many capital letters and small letters:'''
# -----------------------------------------------

# f=open('pythonprograms/filehandling/demo.txt','r')
# e=f.readlines()
# f.seek(0)
# letter=0
# cap=0
# for i in range(len(e)):
#     a=f.readline().strip()
#     for i in a:
#         if i !=' ':
#             if i.isupper():
#                 cap+=1
#             letter+=1
# print("total no of letters : ",letter)
# print("total no of capital letters : ",cap)
# print("toatal no of small letters : ",letter-cap)

'''ouput:'''
# total no of letters :  13
# total no of capital letters :  2
# toatal no of small letters :  


'''how many words:'''
# --------------------

# f=open('pythonprograms/filehandling/demo.txt','r')
# e=f.readlines()
# f.seek(0)
# letter=0
# cap=0
# words=0
# for i in range(len(e)):
#     a=f.readline().strip()
#     s=a.split()
#     for i in s:
#         if i!='':
#             words+=1
#     for i in a:
#         if i !=' ':
#             if i.isupper():
#                 cap+=1
#             letter+=1
# print("total no of letters : ",letter)
# print("total no of capital letters : ",cap)
# print("toatal no of small letters : ",letter-cap)
# print('total no of words : ',words)


'''Number of lines'''
# ----------------------------------
# f=open('pythonprograms/filehandling/demo.txt','r')
# e=f.readlines()
# f.seek(0)
# letter=0
# cap=0
# words=0
# for i in range(len(e)):
#     a=f.readline().strip()
#     s=a.split()
#     for i in s:
#         if i!='':
#             words+=1
#     for i in a:
#         if i !=' ':
#             if i.isupper():
#                 cap+=1
#             letter+=1
# print("total no of letters : ",letter)
# print("total no of capital letters : ",cap)
# print("toatal no of small letters : ",letter-cap)
# print('total no of words : ',words)
# print("no of lines : ",len(e)) ------------*


# append()- a 
# -----------------

# f=open('pythonprograms/filehandling/demo.txt','a')
# f.write('\nusing append')
# f.write('\nsee you')


'''delete text file or a python file:'''
# ------------------------------------

# import os
# os.remove('demo.txt')

'''to check a file is present or not using os:'''
# ------------------------------------
# import os
# if os.path.exists('demo.txt'):
#     print('file found')
# else:
#     print('not')

'''To create a folder -(mkdir)'''
# ---------------------------------

# import os
# os.mkdir('sample.txt')

'''To delete a  folder -(rmdir)'''
# -----------------------------------

# import os
# os.rmdir('sample.txt')