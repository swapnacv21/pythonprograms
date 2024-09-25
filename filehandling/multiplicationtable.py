# f=open('pythonprograms/filehandling/mult.txt','w')
# number=int(input("Enter a number : "))
# for i in range(1,11):
#     # print(i,'*',number,'=',i*number)
#     f.write(str(i)+'*'+str(number)+'='+str(i*number)+'\n')


# f=open('pythonprograms/filehandling/mult.txt','w')
# number=int(input("Enter a number : "))
# for i in range(1,11):
#     print(i,'*',number,'=',i*number)
#     f.write(str(i)+'*'+str(number)+'='+str(i*number)+'\n')


'''task:multiplication table '''
# -----------------------------------------


f=open('pythonprograms/filehandling/mult1.txt','w')
number=int(input("Enter a number : "))
for i in range(1,11):
    for j in range(1,number+1):
        f.write(str(i)+'*'+str(j)+'='+str(j*i)+'\t')
    f.write('\n')
