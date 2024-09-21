# Even numbers in a list:
# ---------------------------------------

'''normal method using for loop:'''

# l=[1,2,3,4,5,6,7,8]
# for i in l:
#     if i%2==0:
#         print(i)


'''1) filter()'''
# -----------
# syntax:
# -----------
'''filter(function,iterable)'''
# -------------------------------



'''using filter() and lambda():'''

# l=[1,2,3,4,5,6,7,8]
# data=filter(lambda x:x%2==0,l)
# print(list(data))

# output:
# [2, 4, 6, 8]

'''2nd method : in single line:'''

# l=[1,2,3,4,5,6,7,8]
# print(list(filter(lambda x:x%2==0,l)))

# output : [2, 4, 6, 8]

'''even numbers in a list using user defined function'''

# l=[1,2,3,4,5,6,7,8]
# def even(x):
#     return x%2==0
# print(list(filter(even,l)))

# output: [2, 4, 6, 8]




'''filter() in string:'''

# l=['apple','orange','kiwi']
# print(list(filter(lambda x:'a' in x,l)))

# output: ['apple', 'orange']

'''using user defined function:'''

# l=['apple','orange','kiwi']
# def fun(x):
#     return 'a' in x
# print(list(filter(fun,l)))

# output: ['apple', 'orange']

'''Odd numbers in a list using filter():'''


# l=[1,2,3,4,5,6,7,8]
# data=filter(lambda x:x%2==1,l)
# print(list(data))

# output: [1, 3, 5, 7]


'''odd numbers using user defined function :'''

# l=[1,2,3,4,5,6,7,8]
# def odd(x):
#     return x%2==1
# print(list(filter(odd,l)))

# output: [1, 3, 5, 7]