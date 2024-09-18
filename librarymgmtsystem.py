user=[]


while True:
    print(
       '''
    1.Registration  
    2.Login
    3.Exit
    '''
    )
    choice=int(input("Enter your choice : "))
    if choice==1:
        name=input("Enter your name : ")
        address=input("Enter your address : ")
        email=input("Enter your email id : ")
        phone=int(input("Enter your phone number : "))
        user.append({'name':name,'address':address,'email':email,'phone':phone})
        print(user)
    elif choice==3:
        break