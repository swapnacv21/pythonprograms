user=[]
library=[]
def register():
    if len(user)==0:
        id=101
    else:
        id=user[-1]['id']+1
    email=input("Enter your email id : ")
    f1=0
    for i in user:                      #--------> checking id already exists or not
        if i['email']==email:
            f1=1
            print("email exists")
            register()
    if f1==0:
        name=input("Enter your name : ")
        address=input("Enter your address : ")
        phone=int(input("Enter your phone number : "))
        password=input("Enter a password : ")
        user.append({'id':id,'name':name,'address':address,'email':email,'phone':phone,'password':password})

def login():
    uname=input("Enter user name : ")
    passw=input("Enter your password : ")
    f=0
    user=''
    if uname=='admin' and passw=='admin':
        f=1
    for i in user:
        if i['email']==uname and i['password']==passw:
            f=2
            user=i
    return f,user

def add_book():
    if len(library)==0:
        book_id=1
    else:
        book_id=library[-1]['book_id']+1
    book_name=input("Enter book name : ")
    book_stock=int(input("Enter stock of book : "))
    book_price=int(input("Enter price of book : "))
    library.append({'book_id':book_id,'book_name':book_name,'book_stock':book_stock,'book_price':book_price})

def view_book():
    print('{:<15}{:<15}{:<15}{:<15}'.format('book_id','book_name','book_stock','book_price'))
    print('-'*70)
    for i in library:
        print('{:<15}{:<15}{:<15}{:<15}'.format(i['book_id'],i['book_name'],i['book_stock'],i['book_price']))


# def update_book():



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
        register()
    elif choice==2:
        f,user=login()
        if f==1:
            while True:
                print(
                    '''
                    1.Add Book
                    2.View Book details
                    3.Update book details
                    4.Delete book
                    5.View user details
                    6.Exit
                    '''
                )
                sub_choice=int(input("Enter your choice : "))
                if sub_choice==1:
                    add_book()
                elif sub_choice==2:
                    view_book()
                elif sub_choice==3:
                    # update
                







        elif f==2:
            print("User login")
        else:
            print("invalid uname or pswd")
    elif choice==3:
        break