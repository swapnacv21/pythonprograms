import sqlite3
con=sqlite3.connect('employee.db')
try:
    con.execute("create table emp(id int,name text,age int,place text,post text,phone_no int)")
except:
    print("table already exists")

while True:
    print(
        '''
        1.Add employee
        2.View employee details
        3.Update employee details
        4.Delete employee 
        5.Search employee
        6.Exit
    '''
    )
    choice=int(input("Enter your choice : "))
    if choice==1:
        id=int(input("Enter employee id : "))
        name=input("Enter employee name : ")
        age=int(input("Enter age of employee : "))
        place=input("Enter place of employee : ")
        post=input("Enter post of employee : ")
        phone=int(input("Enter phone no of employee : "))
        con.execute("insert into emp(id,name,age,place,post,phone_no)values(?,?,?,?,?,?)",(id,name,age,place,post,phone))
        con.commit()
    elif choice==2:
        data=con.execute("select * from emp")
        for i in data:
            print('{:<12}{:<12}{:<12}{:<12}{:<12}{:<12}'.format('id','name','age','place','post','phone_no'))
            print('-'*70)
            for i in data:
                print('{:<12}{:<12}{:<12}{:<12}{:<12}{:<12}'.format(i[0],i[1],i[2],i[3],i[4],i[5]))
    elif choice==3:
        while True:
            print(
                '''
                1.Update employee name
                2.Update age of employee
                3.Update place of employee
                4.Update post of employee
                5.Update phone no of employee
                6.Exit
            '''
            )
            sub_choice=int(input("Enter your choice : "))
            if sub_choice==1:
                old_name=input("enter existing name :") 
                new_name=input("enter new name : ")
                con.execute("update emp set name=? where name=?",(new_name,old_name))
                con.commit()
            elif sub_choice==2:
                old_age=input("enter existing age :") 
                new_age=input("enter new age : ")
                con.execute("update emp set age=? where age=?",(new_age,old_age))
                con.commit()
            elif sub_choice==3:
                old_place=input("enter existing place :") 
                new_place=input("enter new place : ")
                con.execute("update emp set place=? where place=?",(new_place,old_place))
                con.commit()
            elif sub_choice==4:
                old_post=input("enter existing post :") 
                new_post=input("enter new post : ")
                con.execute("update emp set post=? where post=?",(new_post,old_post))
                con.commit()
            elif sub_choice==5:
                old_phone=input("enter existing phone no :") 
                new_phone=input("enter new phone no : ")
                con.execute("update emp set phone_no=? where phone_no=?",(new_phone,old_phone))
                con.commit()
            elif sub_choice==6:
                break
    elif choice==6:
        break