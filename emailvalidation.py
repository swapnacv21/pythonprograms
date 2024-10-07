import re
a='swapnavenu43@gmail.com'

# print(re.search('^[a-z].*@gmail.com$',a))
# output: <re.Match object; span=(0, 22), match='swapnavenu43@gmail.com'>

if re.search('^[a-z].*@gmail.com$',a):
    print("valid")
else:
    print("invalid")

# output: valid
