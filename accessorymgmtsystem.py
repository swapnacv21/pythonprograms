accessories=[]
customers=[]
while True:
    print(
        '''
        1.Admin
        2.Customer
        3.Exit
        '''
    )
    choice=int(input("Enter your choice : "))
    if choice==1:
        while True:
            print(
                '''
                1.Add accessories
                2.View accessories
                3.Update accessories
                4.Delete accessories
                5.Search accessories
                6.View Customer details
                7.Exit
                '''
            )
            sub_choice=int(input("Enter your choice : "))
            if sub_choice==1:
                if len(accessories)==0:
                    id=1
                else:
                    id=accessories[-1]['id']+1
                type=input("Enter type of accessory : ")
                brand=input("Enter brand of accessory : ")
                material=input("Enter accessory material : ")
                price=int(input("Enter price of accessory : "))
                stock=int(input("Enter stock of accessories : "))
                accessories.append({'id':id,'type':type,'brand':brand,'material':material,'price':price,'stock':stock})
            elif sub_choice==2:
                print('{:<5}{:<8}{:<8}{:<12}{:<12}{:<12}'.format('id','type','brand','material','price','stock'))
                print('-'*70)
                for i in accessories:
                    print('{:<5}{:<8}{:<8}{:<12}{:<12}{:<12}'.format(i['id'],i['type'],i['brand'],i['material'],i['price'],i['stock']))
            elif sub_choice==3:
                id=int(input("Enter acessory id : "))
                f=0
                while True:
                    print(
                        '''
                        1.Update accessory type
                        2.Update material of accessory
                        3.Update price
                        4.Update stock
                        5.Exit
                    '''
                    )
                    u_choice=int(input("Enter your choice : "))
                    if u_choice==1:
                        for i in accessories:
                            if i['id']==id:
                                new_type=input("Enter New type : ")
                                i['type']=new_type
                                f=1
                                print("updated")
                        if f==0:
                            print("Invalid id")
                    elif u_choice==2:
                        for i in accessories:
                            if i['id']==id:
                                new_material=input("Enter New material : ")
                                i['material']=new_material
                                f=1
                                print("updated")
                        if f==0:
                            print("Invalid id")
                    elif u_choice==3:
                        for i in accessories:
                            if i['id']==id:
                                new_price=input("Enter New price : ")
                                i['price']=new_price
                                f=1
                                print("updated")
                        if f==0:
                            print("Invalid id")
                    elif u_choice==4:
                        for i in accessories:
                            if i['id']==id:
                                new_stock=input("Enter New stock : ")
                                i['stock']=new_stock
                                f=1
                                print("updated")
                        if f==0:
                            print("Invalid id")
                    elif u_choice==5:
                        break
            elif sub_choice==4:
                id=int(input("Enter your id : "))
                f=0
                for i in accessories:
                    if i['id']==id:
                        accessories.remove(i)
                        f=1
                if f==0:
                    print("Invalid id")
            elif sub_choice==5:
                id=int(input("Enter accessory id : "))
                f=0
                for i in accessories:
                    if i['id']==id:
                        f=1
                        print('{:<5}{:<8}{:<8}{:<12}{:<12}{:<12}'.format('id','type','brand','material','price','stock'))
                        print('{:<5}{:<8}{:<8}{:<12}{:<12}{:<12}'.format(i['id'],i['type'],i['brand'],i['material'],i['price'],i['stock']))
                if f==0:
                        print("Invalid id")
            elif sub_choice==6:
                print('{:<12}{:<12}{:<12}{:<12}'.format('c_id','c_name','c_place','c_phone'))
                print('-'*70)
                for i in customers:
                    print('{:<12}{:<12}{:<12}{:<12}'.format(i['c_id'],i['c_name'],i['c_place'],i['c_phone']))

            elif sub_choice==7:
                break
    elif choice==2:
        while True:
            print(
                '''
                1.Register
                2.View details
                3.Update details
                4.View accessories
                5.buy accessories
                6.Exit
                '''
            )
            customer_choice=int(input("Enter your choice : "))
            if customer_choice==1:
                if len(customers)==0:
                    c_id=1
                else:
                    c_id=customers[-1]['id']+1
                c_name=input("Enter your name : ")
                c_place=input("Enter your place : ")
                c_phone=int(input("Enter your phone number : "))
                customers.append({'c_id':c_id,'c_name':c_name,'c_place':c_place,'c_phone':c_phone,'accessory':[]})
            elif customer_choice==2:
                print('{:<12}{:<12}{:<12}{:<12}'.format('c_id','c_name','c_place','c_phone'))
                print('-'*70)
                for i in customers:
                    print('{:<12}{:<12}{:<12}{:<12}'.format(i['c_id'],i['c_name'],i['c_place'],i['c_phone']))
            elif customer_choice==3:
                id=int(input("Enter your id : "))
                f=0
                while True:
                    print(
                        '''
                        1.Update name
                        2.Update place
                        3.Update phone
                        4.Exit
                    '''
                    )
                    cu_choice=int(input("Enter your choice : "))
                    if cu_choice==1:
                        for i in customers:
                            if i['c_id']==id:
                                new_name=input("Enter New name : ")
                                i['c_name']=new_name
                                f=1
                                print("updated")
                        if f==0:
                            print("Invalid id")
                    elif cu_choice==2:
                        for i in customers:
                            if i['c_id']==id:
                                new_place=input("Enter New place : ")
                                i['c_place']=new_place
                                f=1
                                print("updated")
                        if f==0:
                            print("Invalid id")
                    elif cu_choice==3:
                        for i in customers:
                            if i['c_id']==id:
                                new_phone=input("Enter New phone : ")
                                i['c_phone']=new_phone
                                f=1
                                print("updated")
                        if f==0:
                            print("Invalid id")
                    elif cu_choice==4:
                        break
            elif customer_choice==4:
                print('{:<5}{:<8}{:<8}{:<12}{:<12}{:<12}'.format('id','type','brand','material','price','stock'))
                print('-'*70)
                for i in accessories:
                    print('{:<5}{:<8}{:<8}{:<12}{:<12}{:<12}'.format(i['id'],i['type'],i['brand'],i['material'],i['price'],i['stock']))
            elif customer_choice==5:
                id=int(input("Enter accessory id : "))
                f=0
                for i in accessories:
                    if i['id']==id:
                        f=1
                        if i['stock']>0:
                            customers['accessory'].append(i['id'])
                            i['stock']-=1
                            print("accessory added")
                        else:
                            print("out of stock")
            elif customer_choice==6:
                break
    elif choice==3:
        break