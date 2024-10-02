accessories=[]
def add_acc():
    id=int(input("enter accessory id :"))
    f=0
    for i in accessories:
        if i['id']==id:
            f=1
            print("id exists")
    if f==0:
        type=input("Enter type of accessory : ")
        brand=input("Enter brand of accessory : ")
        material=input("Enter accessory material : ")
        price=int(input("Enter price of accessory : "))
        stock=int(input("Enter stock of accessories : "))
        accessories.append({'id':id,'type':type,'brand':brand,'material':material,'price':price,'stock':stock})
        print("product added successfully")
        # print(accessories)
# add_acc()

def view_acc():
    print('{:<5}{:<8}{:<8}{:<12}{:<12}{:<12}'.format('id','type','brand','material','price','stock'))
    print('-'*70)
    for i in accessories:
        print('{:<5}{:<8}{:<8}{:<12}{:<12}{:<12}'.format(i['id'],i['type'],i['brand'],i['material'],i['price'],i['stock']))
# view_acc()

def update_acc():
    id=int(input("enter accessory id : "))
    f=0
    for i in accessories:
        if i['id']==id:
            f=1
            new_type=input("Enter New type : ")
            new_material=input("Enter New material : ")
            new_price=int(input("Enter New price : "))
            new_stock=input("Enter New stock : ")
            i['type']=new_type
            i['material']=new_material
            i['price']=new_price
            i['stock']=new_stock
            # print(accessories)
    if f==0:
        print("invalid id")
# update_acc()

def delete_acc():
    id=int(input("Enter accessory id : "))
    f=0
    for i in accessories:
        if i['id']==id:
            accessories.remove(i)
            f=1
            # print(accessories)
    if f==0:
        print("Invalid id")
# delete_acc()

def search_acc():
    id=int(input("Enter accessory id : "))
    f=0
    for i in accessories:
        if i['id']==id:
            f=1
            print('{:<5}{:<8}{:<8}{:<12}{:<12}{:<12}'.format('id','type','brand','material','price','stock'))
            print('{:<5}{:<8}{:<8}{:<12}{:<12}{:<12}'.format(i['id'],i['type'],i['brand'],i['material'],i['price'],i['stock']))
    if f==0:
        print("Invalid id")
# search_acc()

# def view_cust():
#     print('{:<12}{:<12}{:<12}{:<12}'.format('c_id','c_name','c_place','c_phone'))
#     print('-'*70)
#     for i in customers:
#         print('{:<12}{:<12}{:<12}{:<12}'.format(i['c_id'],i['c_name'],i['c_place'],i['c_phone']))