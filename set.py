# set:

# to create an empty set use:

# s=set()

# example:
# s=set()
# s1={1,2,3,4,'abc',1}
# print(type(s1))

# output: <class 'set'>

# set removes duplicate values:
# example:

# s=set()
# s1={1,2,3,4,'abc',1}
# print(s1)

# output: {1, 2, 3, 4, 'abc'}

# ----------------------------------

# removing duplicate values from a list using set:

# l=[1,2,3,1,2,3,4]
# s=set(l) ----- converting list into set
# l=list(s) ----- converting set into list
# print(l)

# output: [1, 2, 3, 4]