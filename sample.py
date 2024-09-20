accessories=[]
while True:
    print(
        '''
        1.Add accessories
        2.View
        3.Update
        4.Delete
        5.Search
        6.View customers
        7.Exit
        '''
    )
    choice=input("Enter your choice : ")
    if choice==1:
        id=int(input("Enter"))
        name=input("Enter name of accessory : ")
        brand=input("Enter brand of accessory : ")
        material=input("Enter taccessory material : ")
        price=int(input("Enter price of accessory : "))
        stock=int(input("Enter stock of accessories : "))
        accessories.append({'id':id,'name':name})
