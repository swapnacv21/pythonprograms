import re
a=input("Enter a password : ")
if len(a)>=8 and re.search('^[A-z0-9].*[@#$%&0-9]',a) and not(a.isdigit()):
        print("valid")
else:
    print("invalid")

