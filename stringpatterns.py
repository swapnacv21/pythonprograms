# pattern 1:

# a=65
# for i in range(4):
#     for j in range(4):
#         print(chr(a),end="  ")
#         a+=1
#     print()

# output:
# A  B  C  D  
# E  F  G  H  
# I  J  K  L  
# M  N  O  P  

# -----------------------------------

# pattern 2:

# a=65
# for i in range(4):
#     for j in range(4):
#         print(chr(a),end="  ")
#     print()
#     a+=1

# output:
# A  A  A  A  
# B  B  B  B  
# C  C  C  C  
# D  D  D  D 

# -----------------------------------


# pattern 3:
# a=65
# for i in range(4):
#     for j in range(4):
#         print(chr(a+j),end=" ")
#     print()

# output:
# A B C D 
# A B C D 
# A B C D 
# A B C D 

# -----------------------------------

 
# pattern 4:
# a=65
# for i in range(1,4):
#     for j in range(i):
#         print(chr(a+j),end=" ")
#     print()
    
# output:
# A 
# A B 
# A B C 

# -----------------------------------


#  pattern 5:

# a=65
# for i in range(1,4):
#     for j in range(i):
#         print(chr(a-j),end="  ")
#     print()
#     a+=1

# output:
# A  
# B  A  
# C  B  A

# -----------------------------------


# pattern 6:

# a=65
# for i in range(1,4):
#     for j in range(i):
#         print(chr(a),end="  ")
#     print()
#     a+=1

# output:
# A  
# B  B  
# C  C  C 

# -----------------------------------


# pattern 7:

# b=66
# for i in range(1,5):
#     a=65
#     if i%2==0:
#         for j in range(i):
#             print(chr(b-j),end=" ")
#         b+=2
#     else:
#         for j in range(i):
#             print(chr(a),end=" ")
#             a+=1
#     print()

# output:
# A 
# B A 
# A B C 
# D C B A 

