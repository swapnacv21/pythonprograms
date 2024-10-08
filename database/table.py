'''Database - sqlite3 '''
# ----------------------------

import sqlite3
con=sqlite3.connect('student.db')
try:
    con.execute("create table student_details(roll_no int,name text,age int,mark real)")
except:
    print("Table already exisits")
# con.execute("insert into student_details(roll_no,name,age,mark)values(1,'Aisha',20,97),(2,'aswin',21,80)")
# con.commit()

# roll=int(input("Enter roll no: "))
# name=input("Enter name : ")
# age=int(input("Enter age : "))
# mark=float(input("Enter mark : "))
# con.execute("insert into student_details(roll_no,name,age,mark)values(?,?,?,?)",(roll,name,age,mark))
# con.commit()

# limit=int(input("Enter your limit : "))
# for i in range(limit):
#     roll=int(input("Enter roll no: "))
#     name=input("Enter name : ")
#     age=int(input("Enter age : "))
#     mark=float(input("Enter mark : "))
#     con.execute("insert into student_details(roll_no,name,age,mark)values(?,?,?,?)",(roll,name,age,mark))
#     con.commit()

# data=con.execute("select * from student_details")
# for i in data:
#     print(i)

# output:

# (1, 'Aisha', 20, 97.0)
# (1, 'Aisha', 20, 97.0)
# (2, 'aswin', 21, 80.0)
# (10, 'alan', 24, 90.0)
# (17, 'c', 22, 85.0)
# (21, 'sam', 21, 90.0)
# (22, 'lilly', 21, 78.0)
# (23, 'hanna', 22, 92.0)


# data=con.execute("select * from student_details")  #-------------------> to display all details in a table format
# for i in data:
#     print('{:<12}{:<12}{:<12}{:<12}'.format('roll_no','name','age','mark'))
#     print('-'*50)
#     for i in data:
#         print('{:<12}{:<12}{:<12}{:<12}'.format(i[0],i[1],i[2],i[3]))

# output:

# roll_no     name        age         mark        
# --------------------------------------------------
# 1           Aisha       20          97.0        
# 2           aswin       21          80.0        
# 10          alan        24          90.0        
# 17          c           22          85.0        
# 21          sam         21          90.0        
# 22          lilly       21          78.0        
# 23          hanna       22          92.0 


# data=con.execute("select * from student_details where roll_no=22")  #----------> to select details by a specific condition  example 1
# for i in data:
#     print(i)

# output: (22, 'lilly', 21, 78.0)

#  example 2:

# data=con.execute("select * from student_details where name='aswin'")
# for i in data:
#     print(i)

# output: (2, 'aswin', 21, 80.0)

# user=int(input("enter roll_no: "))
# data=con.execute("select * from student_details")
# for i in data:
#     if i[0]==user:
#         print(i)

# user=int(input("enter roll no: "))
# data=con.execute("select * from student_details where roll_no=?",(user,))
# for i in data:
#     print(i)

# output: enter roll no: 21
# (21, 'sam', 21, 90.0)

# con.execute("update student_details set name='sandra' where name='c'") #--------------> to update a value of a field
# con.commit()

# old_name=input("enter existing name :") #------------------------> to update an existing value based on user input
# new_name=input("enter new name : ")
# data=con.execute("update student_details set name=? where name=?",(new_name,old_name))
# con.commit()

# con.execute("delete from student_details where roll_no=1") #------> deleting a value based on roll_no
# con.commit()

# con.execute("delete from student_details where name='alan'") #------> deleting a value based on name
# con.commit()

# user=int(input("enter roll_no to delete : "))
# data=con.execute("delete from student_details where roll_no=?",(user,)) #--------------------> deleting a value based on user input
# con.commit()

# data=con.execute("select * from student_details where name like 'a%' ") #-------------------> selecting a value based on first letter 
# for i in data:
#     print(i)

# output: (2, 'aswin', 21, 80.0)

# data=con.execute("select * from student_details where name like '%a' ") #------------------------> last letter
# for i in data:
#     print(i)

# output:
# (17, 'sandra', 22, 85.0)
# (23, 'hanna', 22, 92.0)

# data=con.execute("select * from student_details where name like '_a%' ") #------------------------> 2nd letter
# for i in data:
#     print(i)

# output:
# (17, 'sandra', 22, 85.0)
# (23, 'hanna', 22, 92.0)

# data=con.execute("select * from student_details where name like '__l%' ") #------------------------> 3rd letter
# for i in data:
#     print(i)

# output: (22, 'lilly', 21, 78.0)


'''order by'''

# data=con.execute("select * from student_details order by name")  #----------------> displays name in acending order
# for i in data:
#     print(i)

# output:
# (2, 'aswin', 21, 80.0)
# (23, 'hanna', 22, 92.0)
# (22, 'lilly', 21, 78.0)
# (17, 'sandra', 22, 85.0)

# data=con.execute("select * from student_details order by name desc")  #----------------> displays name in descending order
# for i in data:
#     print(i)

# output: 
# (17, 'sandra', 22, 85.0)
# (22, 'lilly', 21, 78.0)
# (23, 'hanna', 22, 92.0)
# (2, 'aswin', 21, 80.0)

'''group by'''

# --> using aggregate functions:

# data=con.execute("select name,max(mark) from student_details group by name")
# for i in data:
#     print(i)

# data=con.execute("select name,min(mark) from student_details group by name")
# for i in data:
#     print(i)

# data=con.execute("select name,count(mark) from student_details group by name")
# for i in data:
#     print(i)
# ====

# data=con.execute("select name,sum(mark) from student_details group by name")
# for i in data:
#     print(i)

# data=con.execute("select name,average(mark) from student_details group by name")
# for i in data:
#     print(i)
# ====