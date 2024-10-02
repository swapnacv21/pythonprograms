customers=[]
def cust_reg():
    c_id=input("enter your id :")
    f=0
    for i in customers:
        if i['c_id']==c_id:
            f=1
            print("id exists")
    if f==0:
        c_name=input("Enter your name : ")
        c_place=input("Enter your place : ")
        c_phone=int(input("Enter your phone number : "))
        customers.append({'c_id':c_id,'c_name':c_name,'c_place':c_place,'c_phone':c_phone,'accessory':[]})

def view_profile():
    print('{:<12}{:<12}{:<12}{:<12}'.format('c_id','c_name','c_place','c_phone'))
    print('-'*70)
    for i in customers:
        print('{:<12}{:<12}{:<12}{:<12}'.format(i['c_id'],i['c_name'],i['c_place'],i['c_phone']))

def update_cust():
    c_id=input("enter your id : ")
    f=0
    for i in customers:
        if i['c_id']==c_id:
            f=1
            new_name=input("Enter New name : ")
            new_place=input("Enter New place : ")
            new_phone=input("Enter New phone : ")
            i['c_name']=new_name
            i['c_place']=new_place
            i['c_phone']=new_phone
    if f==0:
        print("invalid id")


# def view_accessory():
# def buy_accessory():