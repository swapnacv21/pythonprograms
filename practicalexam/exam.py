'''Question 12: To remove duplicates in a list'''
# --------------------------------------------------
# l=[1,2,3,4,5,5,6,7]
# a=[]
# for i in l:
#     if i not in a:
#         a.append(i)
# print(a)
    
'''Question 14 : Print the following pattern'''
# -------------------------------------------------

# a=65
# for i in range(1,5):
#     for j in range(i):
#         print(chr(a-j),end='  ')
#     print()
#     a+=1


'''factorial of a number using function'''
# ------------------------------------------

def factorial():
    a=int(input("enter a number"))
    fact=1
    for i in range(1,a+1):
        fact*=i
    print("factorial is",fact)
factorial()