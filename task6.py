# sum of a list:

# l=[1,2,5,7,8]
# s=0
# for i in l:
#     s+=i
# print(s)

# output: 23

# adding names into a list:

# names=[]
# limit=int(input("How many students?"))
# for i in range(limit):
#     name=input("Enter name :")
#     names.append(name)
# print(names)

# output:
# How many students?5

# Enter name :sona
# Enter name :anu
# Enter name :sonu
# Enter name :sandra
# Enter name :jibin

# ['sona', 'anu', 'sonu', 'sandra', 'jibin']

# deleting duplicate  values:

# l=[1,2,1,5,8,'abc',8,9,9,'abc']
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)

# output: [1, 2, 5, 8, 'abc', 9]

# largest number of the list:

# l=[1,2,10,60,8,5]
# largest=l[0]
# for i in l:
#     if i>largest:
#         largest=i
# print(largest)

# output: 60

# smallest number of a list:

# l=[1,2,10,60,8,5]
# smallest=l[0]
# for i in l:
#     if i<smallest:
#         smallest=i
# print(smallest)

# output: 1

# reverse of strings in a list:

# method 1: using slicing

# l=['apple','orange','mango','kiwi']
# for i in l:
#     print(i[::-1])

# output: 

# elppa
# egnaro
# ognam
# iwik

# method 2: using nested loop

# l=['apple','orange','mango','kiwi']
# for i in l:
#     rev=''
#     for j in i:
#         rev=j+rev
#     print(rev)

# output:

# elppa
# egnaro
# ognam
# iwik