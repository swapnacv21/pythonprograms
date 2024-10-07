import re 

a='abcd'
# print(re.search('a',a))
# OUTPUT: <re.Match object; span=(0, 1), match='a'>

# print(re.search('abcd',a))
# OUTPUT: output: <re.Match object; span=(0, 4), match='abcd'>

# print(re.search('s',a))
# OUTPUT : None

# --------------------------------------------

'''example: 1'''

# if re.search('s',a):
#     print('match')
# else:
#     print("not")

# output: not
# -------------------------------------------

'''example: 2'''

# if re.search('a',a):
#     print("match")
# else:
#     print("not")

# output: match
# --------------------------------------------

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
# --------------------------------------------------------

'''using .. '''

# example:

# print(re.search('a..',a))
# output: <re.Match object; span=(0, 3), match='abc'>

# print(re.search('b..',a))
# <re.Match object; span=(1, 4), match='bcd'>

# print(re.search('c..',a))
# output: None

# ----------------------------------------------------------

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

# ----------------------------------------------------------

'''using + - represents one or more occurance'''

# print(re.search('a.+',a))
# output: <re.Match object; span=(0, 4), match='abcd'>

# print(re.search('b.+',a))
# output: <re.Match object; span=(1, 4), match='bcd'>

# print(re.search('c.+',a))
# output: <re.Match object; span=(2, 4), match='cd'>

# print(re.search('d.+',a))
# output: None

# ----------------------------------------------------------

'''using ? - represents zero or one occurance'''

# print(re.search('a.?',a))
# output: <re.Match object; span=(0, 2), match='ab'>

# print(re.search('b.?',a))
# output : <re.Match object; span=(1, 3), match='bc'>

# print(re.search('c.?',a))
# output: <re.Match object; span=(2, 4), match='cd'>

# print(re.search('d.?',a))
# output: <re.Match object; span=(3, 4), match='d'>
# ----------------------------------------------------------

'''using [] - represents only one value '''
 
# example 1:
# ----------------

# print(re.search('[abcd]',a))
# output: <re.Match object; span=(0, 1), match='a'>

# example 2:
# -----------------

# a='ABCD'

# print(re.search('a-z',a))
# output: None

# print(re.search('[A-Z]',a))
# output: <re.Match object; span=(0, 1), match='A'>

# print(re.search('[A-z]',a))
# output: <re.Match object; span=(0, 1), match='A'>


# example 3:
# -------------------

# a='ABCDefg'
# print(re.search('[A-z]',a))

#output: <re.Match object; span=(0, 1), match='A'>

# example 4:
# ----------------

# a='abABCDefg'

# print(re.search('[A-z]',a))
# output: <re.Match object; span=(0, 1), match='a'>

# print(re.search('[A-M]',a))
# OUTPUT: <re.Match object; span=(2, 3), match='A'>

# print(re.search('[m-z]',a))
# output: None

# example 5:
# --------------

# a='1234'

# print(re.search('[0-9]',a))
# output: <re.Match object; span=(0, 1), match='1'>

# print(re.search('[6-9]',a))
# output: None


# example 6:
# -------------------

# a='abc123'

# print(re.search('[a-z][0-9]',a))
# output: <re.Match object; span=(2, 4), match='c1'>

# a='abcd'

# print(re.search('[a-z][0-9]',a))
# output: None

# a='123456'

# print(re.search('[a-z][0-9]',a))
# output: None 

# print(re.search('[a-z0-9]',a)) #-----------------> or operands
# output: <re.Match object; span=(0, 1), match='1'>



# a='abcdefg1234'

# print(re.search('[a-z0-9]',a))
# output: <re.Match object; span=(0, 1), match='a'>

# print(re.search('[a-z].*[0-9]',a))
# output: <re.Match object; span=(0, 11), match='abcdefg1234'>

a='abcdefg1'

# print(re.search('[a-z].*[0-9]',a))
# output: <re.Match object; span=(0, 8), match='abcdefg1'>

# print(re.search('[a-z].+[0-9]',a))
# output: <re.Match object; span=(0, 8), match='abcdefg1'>

# print(re.search('[a-z].?[0-9]',a))
# <re.Match object; span=(5, 8), match='fg1'>

# print(re.search('[a-z].?[0-9].*',a))
# <re.Match object; span=(5, 8), match='fg1'>

# print(re.search('[a-z].?[0-9].+',a))
# output: none 

# print(re.search('[a-z].?[0-9].?',a))
# <re.Match object; span=(5, 8), match='fg1'>
