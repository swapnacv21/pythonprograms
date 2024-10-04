import re
a='abcd'
# print(re.search('a',a))
# output: <re.Match object; span=(0, 1), match='a'>

# print(re.search('abcd',a))
# output: <re.Match object; span=(0, 4), match='abcd'>

# print(re.search('s',a))
# output: None

'''example: 1'''

# if re.search('s',a):
#     print('match')
# else:
#     print('not')

# output: not

'''example: 2'''

# if re.search('a',a):
#     print('match')
# else:
#     print('not')

# output: match

'''using . - represents a single character'''

# example:

# print(re.search('a.',a))
# output: <re.Match object; span=(0, 2), match='ab'>

# print(re.search('b.',a))
# output: <re.Match object; span=(1, 3), match='bc'>

# print(re.search('c.',a))
# output: <re.Match object; span=(2, 4), match='cd'>

# print(re.search('d.',a))
# output: None

'''using .. '''

# example:

# print(re.search('a..',a))
# output: <re.Match object; span=(0, 3), match='abc'>

# print(re.search('b..',a))
# <re.Match object; span=(1, 4), match='bcd'>

# print(re.search('c..',a))
# output: None


'''using * - represents zero or more occurance'''

# example:

# print(re.search('a.*',a))
# output: <re.Match object; span=(0, 4), match='abcd'>

# print(re.search('b.*',a))
# output: <re.Match object; span=(1, 4), match='bcd'>

# print(re.search('c.*',a))
# output: <re.Match object; span=(2, 4), match='cd'>

# print(re.search('d.*',a))
# output: <re.Match object; span=(3, 4), match='d'>