emp=[]

def login():
    uname=input("Enter user name : ")
    passw=input("Enter password : ")
    f=0
    user=''
    if uname=='admin' and passw=='admin':
        f=1
    for i in emp:
        if i['id']==uname and i['password']==passw:
            f=2
            user=i
    return f,user
def add_emp():
    id=str(input("Enter employee id : "))
    f1=0
    for i in emp:                      #--------> checking id already exists or not
        if i['id']==id:
            f1=1
            print("id exists")
            add_emp()
    if f1==0:
        name=(input("Enter employee name : "))
        age=int(input("Enter employee age : "))
        salary=int(input("Enter salary of employee : "))
        place=(input("Enter place of employee : "))
        dob=(input("Enter date of birth : "))
        pasw=dob
        emp.append({'id':id,'name':name,'age':age,'salary':salary,'place':place,'dob':dob,'password':pasw})
        # print(emp)

def edit_emp():
    id=str(input("Enter employee id : "))
    f1=0
    for i in emp:
        if i['id']==id:
            f1=1
            name=(input("Enter employee name : "))
            age=int(input("Enter employee age : "))
            salary=int(input("Enter salary of employee : "))
            place=(input("Enter place of employee :"))
            dob=(input("Enter date of birth : "))
            i['name']=name
            i['age']=age
            i['salary']=salary
            i['place']=place
            i['dob']=dob
    if f1==0:
        print("Invalid id")
def delete_emp():
    id=str(input("Enter employee id : "))
    f1=0
    for i in emp:
        if i['id']==id:
            f1=1
            emp.remove(i)
    if f1==0:
        print("Invalid id")
def display_emp():
    print('{:<5}{:<8}{:<8}{:<12}{:<12}{:<12}'.format('id','name','age','salary','place','dob'))
    print('-'*70)
    for i in emp:
        print('{:<5}{:<8}{:<8}{:<12}{:<12}{:<12}'.format(i['id'],i['name'],i['age'],i['salary'],i['place'],i['dob']))

def view_profile(user):
    print(user)
def edit_profile(user):
    f1=0
    for i in emp:
        if i['id']==user['id']:
            f1=1
            name=(input("Enter employee name : "))
            age=int(input("Enter employee age : "))
            salary=int(input("Enter salary of employee : "))
            place=(input("Enter place of employee :"))
            dob=(input("Enter date of birth : "))
            i['name']=name
            i['age']=age
            i['salary']=salary
            i['place']=place
            i['dob']=dob
while True:
    print(
        '''
    1.Login
    2.Exit
    '''
    )
    choice=int(input("Enter your choice : "))
    if choice==1:
        f,user=login()
        if f==1:
            while True:
                print(
                    '''
                    1.Add employee
                    2.Update employee
                    3.Delete employee
                    4.Display employee details
                    5.Logout
                    '''
                )
                sub_choice=int(input("Enter your choice : "))
                if sub_choice==1:
                    add_emp()
                elif sub_choice==2:
                    edit_emp()
                elif sub_choice==3:
                    delete_emp()
                elif sub_choice==4:
                    display_emp()
                elif sub_choice==5:
                    break
        elif f==0:
            print('Invalid username or password ')
        elif f==2:
            while True:
                if user['dob']==user['password']:
                    passw=input("Enter new password : ")
                    user['password']=passw
                else:
                    print(
                        '''
                        1.View profile
                        2.Edit profile
                        3.Logout
                        '''
                        )
                    sub_choice=int(input("Enter your choice : "))
                    if sub_choice==1:
                        view_profile(user)
                    elif sub_choice==2:
                        edit_profile(user)
                    elif sub_choice==3:
                        break