# string:
a="welcome"
print(a)
# indexing:
print(a[0])
print(a[6])
print(a[-4])
# slicing:
print(a[0:5])
print(a[-5:-2])
print(a[:5])
print(a[-5:])

print(a[:])

print(a[::2])

print(a[::-1])

# methods of string:
print(a.capitalize())

print(a.center(20))

print(a.count('m'))

print(a.endswith('e'))
print(a.endswith('h'))

print(a.find('e'))
print(a.find('k'))
print(a.find('m'))

print(a.index('e'))
print(a.index("l"))
# print(a.index('k'))

print(a.isdigit())
b='1234'
print(b.isdigit())

print(a.islower())
c='Happy'
print(c.islower())
print(c.isupper())
print(c.upper())
print(c.lower())

d="                      Happy to see you                  "
print(d.split())

print(d.strip())
print(d.lstrip())
print(d.rstrip())

print("{:<10}{:<8}{:<8}".format("Name","Age","Mark"))
print("{:<10}{:<8}{:<8}".format("Jibin","21","85"))
print("{:<10}{:<8}{:<8}".format("Sandra","26","80"))
print("{:<10}{:<8}{:<8}".format("Jessie","20","75"))
