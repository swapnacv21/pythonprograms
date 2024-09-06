# tuple:

# t=(1,2,3,'abc',5.8,1)

# empty tuple:
# t=()

# iterating a tuple:
# t=(1,2,3,'abc',5.8,1)
# for i in t:
#     print(i)

# output:
# 1
# 2
# 3
# abc
# 5.8
# 1

# checking a value is present:

# t=(1,2,3,'abc',5.8,1)
# if 2 in t:
#     print("True")
# else:
#     print("False")

# output:
# True

# index position:

# t=(1,2,3,'abc',5.8,1)
# print(t[0])

# output: 1

# features of tuple:
# 1) consider as tuple even if () is not given

# t=1,2,3,4
# print(t)

# output: (1, 2, 3, 4)

# 2)if we add a , after value its also considered as a tuple

# t=10,
# print(t)

# output: (10,)

# 3) t=(10) considered  as integer because no , is present

# t=(10)
# print(t)

# output: 10


# 4)single value tuple

# t=(10,)

# 5)updating values of a list inside a tuple :

# t=(1,2,[10,11])
# t[2].append(12)
# print(t)

# output: (1, 2, [10, 11, 12]) 
# it will not affect the index of the tuple

# 6) a tuple inside a list can't be changed because it is immutable

# l=[1,2,(10,11)]

# -----------------------------------------------------------------

# updating values in a tuple using typecasting:

# t=(1,2,3,4)
# l=list(t)    ------ converting tuple into list output: [1, 2, 3, 4]
# l.pop()      ------ editing output: [1, 2, 3]
# t=tuple(l)   ------ converting list into tuple back 
# print(t)

# output: (1, 2, 3)

# converting a dictionary to list:

# d={'name':'anu'}
# l=list(d)
# print(l)

# output: ['name'] only keys are changed