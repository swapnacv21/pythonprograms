from admin import *
from customer import *
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
            sub_choice=int(input("enter your choice : "))
            if sub_choice==1:
                add_acc()
            elif sub_choice==2:
                view_acc()
            elif sub_choice==3:
                update_acc()
            elif sub_choice==4:
                delete_acc()
            elif sub_choice==5:
                search_acc()
            # elif sub_choice==6:
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
            c_choice=int(input("Enter your choice : "))
            if c_choice==1:
                cust_reg()
            elif c_choice==2:
                view_profile()
            elif c_choice==3:
                update_cust()
            # elif c_choice==4:
            # elif c_choice==5:
            elif c_choice==6:
                break
    elif choice==3:
        break