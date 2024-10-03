'''POLYMORPHISM'''
# -------------------

# method over riding:

# example 1:

# class school:
#     def notes(self):
#         print("notes in school")
# class student(school):
#     def notes(self):
#         print("notes in student")
# s=student()
# s.notes()


# output: notes in student

# example 2:

# class bank:
#     def __init__(self):
#         print("Add bank details")
# class users(bank):
#     def __init__(self):
#         print("Add user details")
# sbi=bank()
# jo=users()

# output:Add bank details


'''super()'''
# -------------

# example:

# class school:
#     def notes(self):
#         print("notes in school")
# class student(school):
#     def notes(self):
#         super().notes()
#         print("notes in student")
        

# amit=student()
# amit.notes()

'''passing an argument'''
# ------------------------------

# class school:
#     def notes(self,sub):
#         print("notes in school",sub)
# class student(school):
#     def notes(self):
#         super().notes('py')
#         print("notes in student")
        

# amit=student()
# amit.notes()


'''passing a value to parent class using argument:'''
# ------------------------------------------------------

class school:
    def notes(self,sub):
        print("notes in school",sub)
class student(school):
    def notes(self,sub):
        super().notes(sub)
        print("notes in student")
amit=student()
amit.notes('py')