# longest word in a list:

# l=['helo','apple','welcome','python']
# longest=l[0]
# for i in l:
#     if len(i)>len(longest):
#         longest=i
# print(longest)


# pgm to disply palindrome words in a list:
# method 1:

# l=['hello','apple','welcome','python','malayalam','amma']
# for i in l:
#     if i[::-1]==i:
#         print(i)

# method 2:

l=['hello','apple','welcome','python','malayalam','amma']
for i in l:
    a=0
    for j in i:
        f=0
        if i[a]==i[len(i)-a-1]:
            a+=1
        else:
            f=1
            break
    if f==0:
        print(i)



# output:

# malayalam
# amma