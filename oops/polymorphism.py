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