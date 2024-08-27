# dictionary methods:

# 1) clear() - to clear  all items from a dictionary

# d={'name':'anu','age':25,'mark':25}
# d.clear()
# print(d)

# output: {}

#  2) keys() - used to disply keys in a dictionary

# d={'name':'anu','age':25,'mark':25}
# print(d.keys())

# output: dict_keys(['name', 'age', 'mark'])

#  3) values() - used to disply values in a dictionary

# d={'name':'anu','age':25,'mark':25}
# print(d.values())

# output: dict_values(['anu', 25, 25])

# 4) items() - used to disply items in a dictionary

# d={'name':'anu','age':25,'mark':25}
# print(d.items())

# output: dict_items([('name', 'anu'), ('age', 25), ('mark', 25)])

# 5) get() - to find value in a specific key

# d={'name':'anu','age':25,'mark':25}
# print(d.get('name'))
# print(d.get('mark'))

# output: 
# anu
# 25

# # 6) pop() - delete specified key and its value

# d={'name':'anu','age':25,'mark':25}
# d.pop('name')
# print(d)

# output: {'age': 25, 'mark': 25}

# # 7) popitem() - deletes last item in a dictionary

# d={'name':'anu','age':25,'mark':25}
# d.popitem()
# print(d)

# output: {'name': 'anu', 'age': 25}

# # 8) update() - to update a value in a dictionary

# d={'name':'anu','age':25,'mark':25}
# d.update({'name':'ammu'})
# print(d)

# output: {'name': 'ammu', 'age': 25, 'mark': 25}


# 9) setdefault() - used to ceate a key with default value

# d={'name':'anu','age':25,'mark':25}
# d.setdefault('phone')
# print(d)

# output:
# {'name': 'anu', 'age': 25, 'mark': 25, 'phone': None}

# 10)fromkeys() - used to create a dictionary from a list

# d={'name':'anu','age':25,'mark':25}
# l=[1,2,3,4]
# print(d.fromkeys(l))

# output:{1: None, 2: None, 3: None, 4: None}

# 11) copy() - used to copy items in a dictionary to another

# d={'name':'jibin','age':21}
# d1=d.copy()
# print(id(d))
# print(id(d1))
# d1.pop('name')
# print('d=',d)
# print('d1=',d1)

# # output:
# 139789405509056 - id of d
# 139789405267200 -id of d1
# d= {'name': 'jibin', 'age': 21}
# d1= {'age': 21}