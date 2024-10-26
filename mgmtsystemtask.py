library=[]
user=[]
while True:
    print(
        '''
        1.Admin
        2.User
        3.Exit
    '''
    )
    choice=int(input("Enter your choice : "))
    if choice==1:
        while True:
            print(
                '''
                1.Add book
                2.View book details
                3.Update book details
                4.Remove book
                5.Search book
                6.Exit
            '''
            )
            sub_choice=int(input("Enter your choice : "))
            if sub_choice==1:
                book_id=int(input("Enter id of book : "))
                book_name=input("Enter name of book : ")
                book_stock=int(input("Enter stock of book : "))
                book_price=int(input("Enter price of book : "))
                library.append({'book_id':book_id,'book_name':book_name,'book_stock':book_stock,'book_price':book_price})
                print("Book details added successfully...")
                # print(library)
            elif sub_choice==2:
                print('{:<15}{:<15}{:<15}{:<15}'.format('book_id','book_name','book_stock','book_price'))
                print('-'*70)
                for i in library:
                    print('{:<15}{:<15}{:<15}{:<15}'.format(i['book_id'],i['book_name'],i['book_stock'],i['book_price']))

            elif sub_choice==3:
                id=int(input("Enter book id : "))
                f=0
                for i in library:
                    if i['book_id']==id:
                        f=1
                        new_bname=input("Enter new book name : ")
                        new_stock=int(input("Enter new stock : "))
                        new_price=int(input("Enter new price : "))
                        i['book_name']=new_bname
                        i['book_stock']=new_stock
                        i['book_price']=new_price
                        print("Book details updated... ")
                if f==0:
                    print("Invalid book id!")

            elif sub_choice==4:
                id=int(input("Enter book id : "))
                f=0
                for i in library:
                    if i['book_id']==id:
                        f=1
                        library.remove(i)
                        print("Book removed successfully...")

            elif sub_choice==5:
                id=int(input("Enter book id : "))
                f=0
                for i in library:
                    if i['book_id']==id:
                        f=1
                        print('{:<15}{:<15}{:<15}{:<15}'.format('book_id','book_name','book_stock','book_price'))
                        print('{:<15}{:<15}{:<15}{:<15}'.format(i['book_id'],i['book_name'],i['book_stock'],i['book_price']))
                if f==0:
                    print("invalid book id !")

            
            elif sub_choice==6:
                break
    elif choice==2:
        while True:
            print(
                '''
                
                1.View available books
                2.Exit
            '''
            )
            user_choice=int(input("Enter your choice : "))
            if user_choice==1:
                # user_id=int(input("Enter id : "))
                # user_name=input("Enter name : ")
                # user_place=input("Enter place : ")
                # user_phone=int(input("Enter phone : "))
                # user.append({'user_id':user_id,'user_name':user_name,'user_place':user_place,'user_phone':user_phone})
            
                print('{:<15}{:<15}{:<15}{:<15}'.format('book_id','book_name','book_stock','book_price'))
                print('-'*70)
                for i in library:
                    print('{:<15}{:<15}{:<15}{:<15}'.format(i['book_id'],i['book_name'],i['book_stock'],i['book_price']))
            elif user_choice==2:
                break
    elif choice==3:
        break
            


