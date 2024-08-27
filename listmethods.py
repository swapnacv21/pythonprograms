# value adding methods:

# 1)append() :

# l=[]
# l.append(5)
# l.append(10)
# l.append('abcd')
# l.append([20,30,40])
# print(l)

# output: [5, 10, 'abcd', [20, 30, 40]]

# 2)extend()  :

# l=[]
# l.append(5)
# l.append(10)
# l.append('abcd')
# l.append([20,30,40])
# l.extend([1,2,3])
# print(l)

# outpt: [5, 10, 'abcd', [20, 30, 40], 1, 2, 3]

# 3)insert()  :

# l=[]
# l.append(5)
# l.append(10)
# l.append('abcd')
# l.append([20,30,40])
# l.extend([1,2,3])
# l.insert(2,"hello")
# print(l)

# output: [5, 10, 'hello', 'abcd', [20, 30, 40], 1, 2, 3]


# value removing methods:

# 1)clear() :

# l=[10,20,30,'abc']
# l.clear()
# print(l)

#output: []

# 2)pop() :
# example 1:
# ------------

# l=[10,20,30,'abc']
# l.pop()
# print(l)

# output: [10, 20, 30]

# example 2:
# ------------
# l=[10,20,30,'abc']
# l.pop(2)
# print(l)

# output:[10, 20, 'abc']

# 3)remove() :

# l=[10,20,30,'abc']
# l.remove(20)
# print(l)

# output: [10, 30, 'abc']

# ----------------------------

# sort() :

# l=[10,60,30,40]
# l.sort()
# print(l)

# output: [10, 30, 40, 60]


# reverse() :

# l=[10,15,20,'xyz']
# l.reverse()
# print(l)

# output: ['xyz', 20, 15, 10]

# index() :

# l=[10,20,"hello"]
# print(l.index('hello'))

# output: 2

# count() :

# l=[2,4,6,6,'hai']
# print(l.count(6))

# output: 
# 2


# copy()

# l=[1,2,3,4,5]
# l1=l.copy()
# print(id(l))
# print(id(l1))
# l1.pop()
# print('l=',l)
# print('l1=',l1)

# output:
# 140506615182144
# 140506615179648
# l= [1, 2, 3, 4, 5]
# l1= [1, 2, 3, 4]