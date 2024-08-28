# employee management system using dictionary:

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
    choice=int(input("Enter choice : "))
    if choice==1:
        id=int(input("Enter employee id : "))
        name=input("Enter employee name : ")
        age=int(input("Enter age : "))
        phone=int(input("Enter phone number : "))
        place=input("Enter place : ")
        position=input("Enter position of employee : ")
        salary=int(input("Enter salary : "))
        experience=int(input("Enter year of experience : "))        
        employee.append({'id':id,'name':name,'age':age,'phone':phone,'place':place,'position':position,'salary':salary,'experience':experience})
    elif choice==2:
        print('{:<5}{:<8}{:<8}{:<12}{:<12}{:<12}{:<10}{:<5}'.format('id','name','age','phone','place','position','salary','experience'))
        print('-'*70)
        for i in employee:
            print('{:<5}{:<8}{:<8}{:<12}{:<12}{:<12}{:<10}{:<5}'.format(i['id'],i['name'],i['age'],i['phone'],i['place'],i['position'],i['salary'],i['experience']))
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