php=set()
limit=int(input("Enter your limit"))
for i in range(limit):
    name=input("Enter name")
    php.add(name)
print(php)

python=set()
limit=int(input("Enter your limit"))
for i in range(limit):
    name=input("Enter name")
    python.add(name)
print(python)

java=set()
limit=int(input("Enter your limit"))
for i in range(limit):
    name=input("Enter name")
    java.add(name)
print(java)


common=php.intersection(python)
c=common.intersection(java)
print("common name=",c)

unique=python.difference(php)
u=python.difference(java)
stpy=u.intersection(unique)
print("student in python=",stpy)


# output:
# Enter your limit3
# Enter namejibin
# Enter namesandra
# Enter nameswapna
# {'sandra', 'jibin', 'swapna'}
# Enter your limit2
# Enter namejibin
# Enter nameanu 
# {'jibin', 'anu'}
# Enter your limit3
# Enter namejibin
# Enter nameammu
# Enter namelilly
# {'ammu', 'jibin', 'lilly'}
# common name= {'jibin'}
# student in python= {'anu'}


