# class synnefo:
#     def python(self):
#         print("Python in synnefo")
#     def php(self):
#         print("php in synnefo")
#     def registration(self):
#         print("Registration")
# class teaching(synnefo):
#     def notes(self):
#         print("notes")
#     def labs(self):
#         print("labs")
#     def attendence(self):
#         print("attendence")
# class nonteaching(synnefo):
#     def enquiry(self):
#         print("enquiry")
#     def account(self):
#         print("account")
# class student(teaching):
#     def lab(self):
#         print("lab")
#     def system_availability(self):
#         print("system availability")
# std1=student()
# std1.attendence()
# std1.labs()
# std1.notes()


# example 2:

class cafe:
    def details(self):
        print("Details of cafe")
    def contact(self):
        print("Contact number")
    def location(self):
        print("Location of cafe")
class owner(cafe):
    def staff_details(self):
        print("staff details")
    def accounts(self):
        print("accounts details")
class items(cafe):
    def burger(self):
        print("burger")
    def shakes(self):
        print("shakes")
    def mojitos(self):
        print("mojitos")
    def sandwich(self):
        print("sandwich")
class staff(owner):
    def billing_staff(self):
        print("billing staff details")
    def kitchen_staff(self):
        print("kitchen staff details")
    def cleaning_staff(self):
        print("cleaning staff details")
class customer(items):
    def buy(self):
        print("buy items")
    def online(self):
        print("buy items online")
    def feedback(self):
        print("customer feedback")
c=customer()
c.contact()
c.online()
s=staff()
s.location()