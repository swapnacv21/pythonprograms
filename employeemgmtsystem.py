import datetime
employee=[]
while True:
    print(
        '''
    1.Registration
    2.View employee list
    3.Update employee details
    4.Delete employee
    5.Tasks
    6.Search
    7.Exit
    '''
    )
    choice=int(input("Enter choice"))
    if choice==1:
        id=int(input("Enter employee id : "))
        name=input("Enter employee name : ")
        age=int(input("Enter age : "))
        phone=int(input("Enter phone number : "))
        place=input("Enter place : ")
        position=input("Enter position of employee : ")
        salary=int(input("Enter salary : "))
        experience=int(input("Enter year of experience : "))
        employee.append([id,name,age,phone,place,position,salary,experience])
    elif choice==2:
        print('{:<5}{:<8}{:<8}{:<12}{:<12}{:<12}{:<10}{:<5}'.format('id','name','age','phone','place','position','salary','experience'))
        print('-'*70)
        for i in employee:
            print('{:<5}{:<8}{:<8}{:<12}{:<12}{:<12}{:<10}{:<5}'.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
    elif choice==3:
        id=int(input("Enter employee id : "))
        f=0
        while True:
            print(
                '''
            1.Update age
            2.Update phone number
            3.Update place
            4.Update position
            5.Update salary
            6.Update experience
            7.Exit
            '''
            )
            choice=int(input("Enter choice"))
            if choice==1:
                for i in employee:
                    if id in i:
                        new_age=int(input("Enter new age"))
                        i[2]=new_age
                        f=1
                if f==0:
                    print("Invalid id")
            elif choice==2:
                for i in employee:
                    if id in i:
                        new_phone_no=int(input("Enter new phone number"))
                        i[3]=new_phone_no
                        f=1
                if f==0:
                    print("Invalid id")
            elif choice==3:
                for i in employee:
                    if id in i:
                        new_place=input("Enter new place")
                        i[4]=new_place
                        f=1
                if f==0:
                    print("Invalid id")
            elif choice==4:
                for i in employee:
                    if id in i:
                        new_position=input("Enter new position")
                        i[5]=new_position
                        f=1
                if f==0:
                    print("Invalid id")
            elif choice==5:
                for i in employee:
                    if id in i:
                        new_salary=int(input("Enter new salary"))
                        i[6]=new_salary
                        f=1
                if f==0:
                    print("Invalid id")
            elif choice==6:
                for i in employee:
                    if id in i:
                        update_experience=int(input("Enter  experience : "))
                        i[7]=update_experience
                        f=1
                if f==0:
                    print("Invalid id")
            elif choice==7:
                break
            else:
                print("Invalid choice")
    elif choice==4:
        id=int(input("Enter employee id : "))
        f=0
        for i in employee:
            if id in i:
                employee.remove(i)
                f=1
        if f==0:
            print("Invalid id")
    elif choice==5:
        id=int(input("Enter employee id : "))
        f=0
        for i in employee:
            if id in i:
                f=1
                task=input("Enter task : ")
                date=datetime.datetime.now().strftime("%x")
                days=int(input("How many days? "))
                i.append([task,date,days])
        if f==0:
            print("Invalid id")
    elif choice==6:
        id=int(input("Enter employee id : "))
        f=0
        for i in employee:
            if id in i:
                f=1
                print('{:<5}{:<8}{:<8}{:<12}{:<12}{:<12}{:<10}{:<5}'.format('id','name','age','phone','place','position','salary','experience'))
                print('{:<5}{:<8}{:<8}{:<12}{:<12}{:<12}{:<10}{:<5}'.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
                print("Work details :")
                if len(i)==9:
                    print(i[8])
                else:
                    print("No work")
        if f==0:
            print("Invalid id")
    elif choice==7:
        break
    else:
        print("Invalid choice")




