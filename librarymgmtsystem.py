user=[]
library=[]
def register():
    if len(user)==0:
        id=101
    else:
        id=user[-1]['id']+1
    email=input("Enter your Email id : ")
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
        user.append({'id':id,'name':name,'address':address,'email':email,'phone':phone,'password':password,'books':[]})

def login():
    uname=input("Enter user name : ")
    passw=input("Enter your password : ")
    f=0
    u=''
    if uname=='admin' and passw=='admin':
        f=1
    for i in user:
        if i['email']==uname and i['password']==passw:
            f=2
            u=i
    return f,u

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


def update_book():
    id=int(input("enter book id : "))
    f=0
    for i in library:
        if i['book_id']==id:
            f=1
            name=input("name of the book : ")
            stock=int(input("Enter stock of the book : "))
            price=int(input("Enter price of the book : "))
            i['book_name']=name
            i['book_stock']=stock
            i['book_price']=price
        
    if f==0:
        print("Invalid id")
     

def delete_book():
    id=int(input("Enter book id : "))
    f=0
    for i in library:
        if i['book_id']==id:
            f=1
            library.remove(i)
    if f==0:
        print("Invalid book id")

def view_user():
    print('{:<5}{:<8}{:<8}{:<12}{:<12}'.format('id','name','email','phone','address'))
    print('-'*70)
    for i in user:
        print('{:<5}{:<8}{:<8}{:<12}{:<12}'.format(i['id'],i['name'],i['email'],i['phone'],i['address']))

def view_profile(user):
    print('{:<5}{:<8}{:<8}{:<12}{:<12}'.format('id','name','email','address','phone'))
    print('-'*70)
    print('{:<5}{:<8}{:<8}{:<12}{:<12}'.format(user['id'],user['name'],user['email'],user['address'],user['phone']))

def view_books():
    print('{:<15}{:<15}{:<15}{:<15}'.format('book_id','book_name','book_stock','book_price'))
    print('-'*70)
    for i in library:
        print('{:<15}{:<15}{:<15}{:<15}'.format(i['book_id'],i['book_name'],i['book_stock'],i['book_price']))

def take_book(user):
    id=int(input("Enter book id : "))
    f=0
    for i in library:
        if i['book_id']==id:
            f=1
            if i['book_stock']>0:
                u['books'].append(i['book_id'])
                i['book_stock']-=1
                print("book added")
            else:
                print("out of stock")

def  return_book(u):
    id=int(input("Enter book id : "))
    f=0
    for i in library:
        if i['book_id']==id and id in u['books']:
            f=1
            i['book_stock']+=1
            u['books'].remove(id)
            print("book returned")
    if f==0:
        print("book not found")

def books_in_hand(u):
    print(u['books'])

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
        f,u=login()
        if f==1:
            while True:
                print(
                    '''
                    1.Add Book
                    2.View Book details
                    3.Update book details
                    4.Delete book
                    5.View user details
                    6.Logout
                    '''
                )
                sub_choice=int(input("Enter your choice : "))
                if sub_choice==1:
                    add_book()
                elif sub_choice==2:
                    view_book()
                elif sub_choice==3:
                    update_book()
                elif sub_choice==4:
                    delete_book()
                elif sub_choice==5:
                    view_user()
                elif sub_choice==6:
                    break
        elif f==2:
            while True:
                print(
                    '''
                    1.View profile
                    2.View books
                    3.Take books
                    4.Return book
                    5.Books in hand
                    6.Logout
                    '''
                )
                sub_choice=int(input("Enter your choice : "))
                if sub_choice==1:
                    view_profile(u)
                elif sub_choice==2:
                    view_books()
                elif sub_choice==3:
                    take_book(u)
                elif sub_choice==4:
                    return_book(u)
                elif sub_choice==5:
                    books_in_hand(u)
                elif sub_choice==6:
                    break
        else:
            print("Invalid username or password !")
    elif choice==3:
        break