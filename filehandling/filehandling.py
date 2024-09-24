f=open('pythonprograms/filehandling/demo.txt','a')

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

# d=f.readlines()
# f.seek(0)
# for i in range(len(d)):
#     a=f.readline().strip()
#     print(a[::-1])
    # print(a)

f.write('happy birthday \n')
f.write('namaste')
