# example 1:

# for i in range(11):
#     print(i)

# example 2 - using starting and ending value:

# for i in range(1,11):
#     print(i)

# example 3 - using increment:

# for i in range(1,11,2):
#     print(i)

# question 1) Natural numbers between two values:

# a,b=int(input("enter a number")),int(input("enter a number"))
# for i in range(a,b):
#     print(i)

# question 2) Sum of n numbers:
# a,b=int(input("enter 1st number")),int(input("enter 2nd number"))
# s=0
# for i in range(a,b):
#     s+=i
#     print(s)

# question 3) Even numbers:

# a,b=int(input("enter a no")),int(input("enter a no"))
# for i in range(a,b):
#     if i%2==0:
#         print(i)

# question 4) odd numbers:

# a,b=int(input("enter a no")),int(input("enter a no"))
# for i in range(a,b):
#      if i%2==1:
#          print(i)

# question 5) factorial:
# a=int(input("enter a number"))
# fact=1
# for i in range(1,a+1):
#         fact*=i
# print("factorial is",fact)

# question 6) multiplication table:

a=int(input("enter a number"))
for i in range(1,11):
    print(a,"*",i,"=",a*i)

# question 7) reverse of a number:

# a=int(input("enter a number"))
# rev=0
# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10
# print(rev)