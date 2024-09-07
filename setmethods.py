# Set Methods:

# 1) add() - to add element to a set

# s={1,2,3,4}
# s.add(5)
# print(s)

# output: {1, 2, 3, 4, 5}

# 2) clear() - to clear the set

# s={1,2,3,4}
# s.clear()
# print(s)

# output:empty set

# 3) copy() - to copy a set

# s={1,2,3,4}
# s1=s.copy()
# print("s= ",s)
# print("s1= ",s1)

# output:
# s=  {1, 2, 3, 4}
# s1=  {1, 2, 3, 4}

# 4) difference()

# s={10,1,2,3}
# s1={1,10,5,6}
# print(s.difference(s1))

# 5) discard()

# s={1,2,3,4}
# s.discard(4)
# print(s)

# output: {1, 2, 3}

# 6) remove()

# s={1,2,3,4}
# s.remove(3)
# print(s)

# output: {1, 2, 4}

# 7) pop()

# s={1,2,3,4}
# s.pop()
# print(s)

# doubt------------------
# output:{2, 3, 4}

# 8) update()

# s={1,2,3,4}
# s.update({10,11,12,1})
# print(s)

# ouput: {1, 2, 3, 4, 10, 11, 12}

# ---------------------------------------

# 9) intersection()

# s={1,2,3,4,5,6}
# s1={1,2,3,10,11}
# print(s.intersection(s1))


# output: {1, 2, 3}

# 10) union()

# s={1,2,3,4}
# s1={10,11,12}
# print(s.union(s1))

# output: {1, 2, 3, 4, 10, 11, 12}

# 11) isdisjoint()

# s={1,2,3,4}
# s1={10,11,12}
# print(s.isdisjoint(s1))

# output 1: True

# s={1,2,3,4}
# s1={1,2,5,6,7}
# print(s.isdisjoint(s1))

# output 2: False

# 12) issubset()

# s={1,2,3,4}
# s1={1,2,3}
# print(s1.issubset(s))

# output: True

# 13) issuperset()

# s={1,2,3,4}
# s1={1,2,3,7,9,8}
# print(s.issuperset(s1))

# output: False

# 14) symmetric_difference()

# s={1,2,3,4,5,6}
# s1={1,2,3,4,7,8}
# print(s.symmetric_difference(s1))

# output: {5, 6, 7, 8}

# 15) difference_update()

# s={1,2,3,4,5}
# s1={1,2,3,6,7}
# s.difference_update(s1)
# print("s=",s)

# output: s= {4, 5}

# 16) intersection_update()

# s={1,2,3,4,5}
# s1={1,2,3,6,7}
# s.intersection_update(s1)
# print("s=",s)

# output: s= {1, 2, 3}

# 17) symmetric_difference_update()

# s={1,2,3,4,5}
# s1={1,2,3,6,7}
# s.symmetric_difference_update(s1)
# print("s=",s)

# output: s= {4, 5, 6, 7}