# shop management system :

import datetime
employee=[]
product=[]
while True:
    print(
        '''
    1.Employee details
    2.Product details
    3.Exit
    '''
    )
    choice=int(input("Enter your choice"))
    if choice==1:
        while True:
            print(
                '''
            1.Registration
            2.View employee list
            3.Update employee details
            4.Delete employee
            5.Search
            6.Exit
            '''
            )
            choice=int(input("Enter your choice"))
            if choice==1:
                id=int(input("Enter employee id : "))
                name=input("Enter employee name : ")
                age=int(input("Enter age : "))
                phone=int(input("Enter phone number : "))
                place=input("Enter place : ")
                position=input("Enter position of employee : ")
                salary=int(input("Enter salary : "))
                experience=int(input("Enter year of experience : "))        
                employee.append({'id':id,'name':name,'age':age,'phone':phone,'place':place,'position':position,'salary':salary,'experience':experience})
            elif choice==2:
                print('{:<5}{:<8}{:<8}{:<12}{:<12}{:<12}{:<10}{:<5}'.format('id','name','age','phone','place','position','salary','experience'))
                print('-'*70)
                for i in employee:
                    print('{:<5}{:<8}{:<8}{:<12}{:<12}{:<12}{:<10}{:<5}'.format(i['id'],i['name'],i['age'],i['phone'],i['place'],i['position'],i['salary'],i['experience']))
            elif choice==3:
                id=int(input("Enter employee id : "))
                f=0
                while True:
                    print(
                        '''
                        1.Update age
                        2.Update phone number
                        3.Update place
                        4.Update position
                        5.Update salary
                        6.Update experience
                        7.Exit
                        '''
                        )
                    choice=int(input("Enter choice"))
                    if choice==1:
                        for i in employee:
                            if i['id']==id:
                                new_age=int(input("Enter new age"))
                                i['age']=new_age
                                f=1
                                if f==0:
                                    print("Invalid id")
                    elif choice==2:
                        for i in employee:
                            if i['id']==id:
                                new_phone_no=int(input("Enter new phone number"))
                                i['phone']=new_phone_no
                                f=1
                        if f==0:
                            print("Invalid id")
                    elif choice==3:
                        for i in employee:
                            if i['id']==id:
                                new_place=input("Enter new place")
                                i['place']=new_place
                                f=1
                        if f==0:
                            print("Invalid id")
                    elif choice==4:
                        for i in employee:
                            if i['id']==id:
                                new_position=input("Enter new position")
                                i['position']=new_position
                                f=1
                        if f==0:
                            print("Invalid id")
                    elif choice==5:
                        for i in employee:
                            if i['id']==id:
                                new_salary=int(input("Enter new salary"))
                                i['salary']=new_salary
                                f=1
                        if f==0:
                            print("Invalid id")
                    elif choice==6:
                        for i in employee:
                            if i['id']==id:
                                update_experience=int(input("Enter  experience : "))
                                i['experience']=update_experience
                                f=1
                        if f==0:
                            print("Invalid id")
                    elif choice==7:
                        break
                    else:
                        print("Invalid choice")
            elif choice==4:
                id=int(input("Enter employee id : "))
                f=0
                for i in employee:
                    if i['id']==id:
                        employee.remove(i)
                        f=1
                if f==0:
                    print("Invalid id")
            elif choice==5:
                id=int(input("Enter employee id : "))
                f=0
                for i in employee:
                    if i['id']==id:
                        f=1
                        print('{:<5}{:<8}{:<8}{:<12}{:<12}{:<12}{:<10}{:<5}'.format('id','name','age','phone','place','position','salary','experience'))
                        print('{:<5}{:<8}{:<8}{:<12}{:<12}{:<12}{:<10}{:<5}'.format(i['id'],i['name'],i['age'],i['phone'],i['place'],i['position'],i['salary'],i['experience']))
                if f==0:
                        print("Invalid id")
            elif choice==6:
                break
            else:
                print("Invalid choice")



    elif choice==2:
        while True:
            print(
                '''
            1.Add Product
            2.View Product
            3.Update Product Details
            4.Remove product
            5.Search product
            6.Exit
            '''
            )
            choice=int(input("Enter your choice : "))
            if choice==1:
                productid=int(input("Enter product id : "))
                productname=input("Enter product name : ")
                producttype=input("Enter product type: ")
                productprice=int(input("Enter price of the product : "))
                productstock=int(input("Enter stock of the product : "))
                product.append({'productid':productid,'productname':productname,'producttype':producttype,'productprice':productprice,'productstock':productstock})
            elif choice==2:
                print('{:<15}{:<15}{:<15}{:<15}{:<15}'.format('productid','productname','producttype','productprice','productstock'))
                print('-'*70)
                for i in product:
                    print('{:<15}{:<15}{:<15}{:<15}{:<15}'.format(i['productid'],i['productname'],i['producttype'],i['productprice'],i['productstock']))
            elif choice==3:
                productid=int(input("Enter product id : "))
                f=0
                while True:
                    print(
                        '''
                        1.Update product name
                        2.Update product type
                        3.Update product price
                        4.Update product stock
                        5.Exit
                        '''
                        )
                    choice=int(input("Enter choice"))
                    if choice==1:
                        for i in product:
                            if i['productid']==productid:
                                new_name=(input("Enter new product name"))
                                i['productname']=new_name
                                f=1
                        if f==0:
                            print("Invalid id")
                    elif choice==2:
                        for i in product:
                            if i['productid']==productid:
                                new_type=(input("Enter new product type"))
                                i['producttype']=new_type
                                f=1
                        if f==0:
                            print("Invalid id")
                    elif choice==3:
                        for i in product:
                            if i['productid']==productid:
                                new_price=(input("Enter new product price"))
                                i['productprice']=new_price
                                f=1
                        if f==0:
                            print("Invalid id")
                    elif choice==4:
                        for i in product:
                            if i['productid']==productid:
                                new_stock=(input("Enter new product stock"))
                                i['productstock']=new_stock
                                f=1
                        if f==0:
                            print("Invalid id")

                    elif choice==5:
                        break
                    
    elif choice==3:
        break
    else:
        print("Invalid choice")        