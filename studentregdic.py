# student management system using dictionary :

std=[]
while True:
    print(
        '''
    1)Add student
    2)View student details
    3)Update student details
    4)Delete
    5)Exit
    '''
    )
    while True:
        try:
            choice=int(input("Enter choice : "))
            break
        except:
            print("Invalid choice")
            print("Enter the correct choice")
    if choice==1:
        name=str(input("Enter name : "))
        age=int(input("Enter age : "))
        mark=int(input("Enter mark : "))
        std.append({'name':name,'age':age,'mark':mark})
    elif choice==2:
        print('{:<10}{:<8}{:<8}'.format('name','age','mark'))
        print('-'*25)
        for i in std:
            print('{:<10}{:<8}{:<8}'.format(i['name'],i['age'],i['mark']))
    elif choice==3:
        name=input("Enter name")
        f=0
        for i in std:
            if i['name']==name:
                new_mark=int(input("Enter mark"))
                i['mark']=new_mark
                f=1
        if f==0:
            print("Name is not in list")
    elif choice==4:
        name=input("Enter name")
        f=0
        for i in std:
            if i['name']==name:
                std.remove(i)
                f=1
        if f==0:
            print("Name not in list")
    elif choice==5:
        break
    else:
        print("Invalid choice")







