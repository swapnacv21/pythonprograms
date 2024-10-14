import mysql.connector
con=mysql.connector.connect(host='localhost',user='batch11',password='batch11',database='studentdatas')
con.autocommit=True
cur=con.cursor()
# cur.execute('create database studentdatas')    #-----------------> creating database
# cur.execute("create table student (roll_no int,name text,age int)")     #----------> creating table
# cur.execute("insert into student (roll_no,name,age) values(1,'aswin',20)")    #---------> inserting value into the table

# rollno=int(input("enter roll no : "))
# name=input("enter name : ")
# age=int(input("enter age : "))
# cur.execute("insert into student (roll_no,name,age) values(%s,%s,%s)",(rollno,name,age))   #-------> inserting values into table by user input

# cur.execute("select * from student")  #------> to display deatils
# data=cur.fetchall()
# for i in data:
#     print(i)



# cur.execute("update student set name='Aswin' where name='aswin'") #--------------> to update a value of a field

# old_name=input("Enter old name : ")
# new_name=input("Enter new name : ")
# cur.execute("update student set name=%s where name=%s",(new_name,old_name))

# delete,orderby,like,groupby