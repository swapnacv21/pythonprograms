# pattern 1:

# for i in range(3):
#     for j in range(3):
#         print("*",end="  ")
#     print()

# output: 
# *  *  *  
# *  *  *  
# *  *  * 


# pattern 2:

# for i in range(3):
#     for j in range(1,4):
#         print(j,end="  ")
#     print()

# output:
# 1  2  3  
# 1  2  3  
# 1  2  3  


# pattern 3:

# for i in range(5):
#     if i%2==0:
#         for j in range(3):
#             print(i,end="  ")
#         print()
   
# output:
# 0 0 0 
# 2 2 2 
# 4 4 4 

# pattern 4:

# a=0
# for i in range(3):
#     for j in range(3):
#         print(a,end="  ")
#         a+=1
#     print()

# output:
# 0  1  2  
# 3  4  5  
# 6  7  8  

# pattern 5:

# for i in range(3):
#     a=i
#     for j in range(3):
#         print(a,end="  ")
#         a+=1
#     print()

# output:
# 0  1  2  
# 1  2  3  
# 2  3  4  


# pattern 6:

# for i in range(3):
#     # print("i=",i)
#     a=i+i
#     for j in range(3):
#         print(a,end="  ")
#         a+=1
#     print()

# output:
# 0  1  2  
# 2  3  4  
# 4  5  6  

# pattern 7:


# for i in range(4):
#     if i%2==0:
#         for j in range(3):
#             print(j,end=" ")
#     else:
#         for j in range(3):
#             print(2-j,end=" ")
#     print()
    
# output:
# 0 1 2 
# 2 1 0 
# 0 1 2 
# 2 1 0 


# pattern 8:

for i in range(3):
        for j in range(3):
            j%2==1
            print(j*j,end="  ")
        print()
