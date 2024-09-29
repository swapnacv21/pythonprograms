# class Bank:
#     def __init__(self):
#         self.bal=0
#     def deposit(self,amt):
#         self.bal+=amt
#         print("Amount added")
#     def withdraw(self,amt):
#         self.bal-=amt
#         print("Amount withdraw")
#     def display(self):
#         print("remaining balance : ",self.bal)
# user1=Bank()
# user1.deposit(10000)
# user1.withdraw(2000)
# user1.display()


'''output:
Amount added
Amount withdraw
remaining balance :  8000'''

# user2=Bank()
# user2.deposit(1000)
# user2.withdraw(4000)
# user2.display()
'''
output:
Amount added
Amount withdraw
remaining balance :  -3000'''

# ---------------------------------------------------------------------------------------

'''sample program using types of arguments:'''
# ------------------------------------------

'''1)positional argument:'''

# class Demo:
#     def __init__(self,a):
#         print("a=",a)
# obj=Demo(10)

# output: a= 10
'''2) Keyword argument : '''

# class Demo:
#     def __init__(self,a,b):
#         print("1st=",a)
#         print("2nd=",b)
# obj=Demo(a=10,b=12)

# output:
# 1st= 10
# 2nd= 12
'''3) Arbitary argument :'''

# class Demo:
#     def __init__(self,*a):
#         print("a=",a)
# obj=Demo(500,1000)

# output: a= (500, 1000)


'''4) Default argument : '''

# class Demo:
#     def __init__(self,name='swapna',amount=2000):
#         print(name,amount)
# obj=Demo('Aswin')
# obj=Demo('Anu',25000)
# obj=Demo(amount=22000)

# output:

# Aswin 2000
# Anu 25000
# swapna 22000

'''5) Arbitory keyword argument : '''

class Demo:
    def __init__(self,**a):
        print("a=",a)
obj=Demo(name='swapna',amount=20000)

output: a= {'name': 'swapna', 'amount': 20000}