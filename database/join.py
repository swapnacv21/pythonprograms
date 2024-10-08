import sqlite3
con=sqlite3.connect('std.db')
try:
    con.execute("create table std_details(roll_no int,name text,age int)")
except:
    print("table exists")

# con.execute("insert into std_details(roll_no,name,age)values(1,'Aisha',20),(2,'Aswin',21),(3,'Anamika',22)")
# con.commit()

try:
    con.execute("create table mark(roll_no int,sub text,mark real)")
except:
    print("table exists")

# con.execute("insert into mark(roll_no,sub,mark)values(1,'Python',88),(2,'php',90),(3,'java',75),(1,'php',98)")
# con.commit()

# inner join:

# data=con.execute("select std_details.roll_no,std_details.name,std_details.age,mark.sub,mark.mark from std_details join mark on std_details.roll_no=mark.roll_no")
# for i in data:
#     print(i)

# output:
# (1, 'Aisha', 20, 'Python', 88.0)
# (1, 'Aisha', 20, 'php', 98.0)
# (2, 'Aswin', 21, 'php', 90.0)
# (3, 'Anamika', 22, 'java', 75.0)

# left join:

# data=con.execute("select std_details.roll_no,std_details.name,std_details.age,mark.sub,mark.mark from std_details left join mark on std_details.roll_no=mark.roll_no")
# for i in data:
#     print(i)

# right join:

# data=con.execute("select std_details.roll_no,std_details.name,std_details.age,mark.sub,mark.mark from mark left join std_details on std_details.roll_no=mark.roll_no")
# for i in data:
#     print(i)

# output:
# (1, 'Aisha', 20, 'Python', 88.0)
# (2, 'Aswin', 21, 'php', 90.0)
# (3, 'Anamika', 22, 'java', 75.0)
# (1, 'Aisha', 20, 'php', 98.0)
# (None, None, None, 'java', 65.0)

# cross join:

# data=con.execute("select std_details.roll_no,std_details.name,std_details.age,mark.sub,mark.mark from mark cross join std_details")
# for i in data:
#     print(i)

# # output:
# (1, 'Aisha', 20, 'Python', 88.0)
# (2, 'Aswin', 21, 'Python', 88.0)
# (3, 'Anamika', 22, 'Python', 88.0)
# (1, 'Aisha', 20, 'php', 90.0)
# (2, 'Aswin', 21, 'php', 90.0)
# (3, 'Anamika', 22, 'php', 90.0)
# (1, 'Aisha', 20, 'java', 75.0)
# (2, 'Aswin', 21, 'java', 75.0)
# (3, 'Anamika', 22, 'java', 75.0)
# (1, 'Aisha', 20, 'php', 98.0)
# (2, 'Aswin', 21, 'php', 98.0)
# (3, 'Anamika', 22, 'php', 98.0)
# (1, 'Aisha', 20, 'java', 65.0)
# (2, 'Aswin', 21, 'java', 65.0)
# (3, 'Anamika', 22, 'java', 65.0)