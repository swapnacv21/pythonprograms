student=[]
while True:
    print(
        '''
    1.Add
    2.View
    3.Update
    4.Delete
    5.Exit
    '''
    )
    choice=int(input("Enter choice"))
    if choice==1:
        name=input("Enter your name")
        age=input("Enter your age")
        mark=input("Enter your mark")
        student.append([name,age,mark])
    elif choice==2:
        print('{:<10}{:<8}{:<8}'.format('name','age','mark'))
        print('-'*25)
        for i in student:
            print('{:<10}{:<8}{:<8}'.format(i[0],i[1],i[2]))
    elif choice==3:
        name=input("Enter name")
        f=0
        for i in student:
            if name in i:
                new_mark=int(input("Enter mark"))
                i[2]=new_mark
                f=1
        if f==0:
            print("Name is not in list")
    elif choice==4:
        name=input("Enter name")
        f=0
        for i in student:
            if name in i:
                student.remove(i)
                f=1
        if f==0:
            print("Name not in list")
    elif choice==5:
        break
    else:
        print("Invali choice")



