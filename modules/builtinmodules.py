# (1) datetime
# -----------------

# method 1:

# import datetime
# print(datetime.datetime.now())

'''output: 2024-09-23 12:31:48.419494'''

# method 2:


# from datetime import datetime
# print(datetime.now())


'''output: 2024-09-23 12:31:48.419494'''

# -------------------------------------------


'''1) %a  - prints day in short'''
# -------------------------------
# import datetime
# print(datetime.datetime.now().strftime('%a'))

# output: Mon


'''2) %A'''
# --------------------------

# import datetime
# print(datetime.datetime.now().strftime('%A'))

# OUTPUT : Monday


'''3) %d'''
# -------------------

# import datetime
# print(datetime.datetime.now().strftime('%d'))

# OUTPUT:23

'''4) %b'''
# ---------------------

# import datetime
# print(datetime.datetime.now().strftime('%b'))

# OUTPUT: Sep

'''5) %B'''
# --------------------

# import datetime
# print(datetime.datetime.now().strftime('%B'))

# OUTPUT: September

'''6) %m'''
# ----------------------

# import datetime
# print(datetime.datetime.now().strftime('%m'))

# OUTPUT: 09

'''7) %y'''
# -----------------

# import datetime
# print(datetime.datetime.now().strftime('%y'))

# OUTPUT: 24

'''8) %Y '''
# ----------

# import datetime
# print(datetime.datetime.now().strftime('%Y'))

# OUTPUT: 2024

'''9) %x '''
# ----------------

# import datetime
# print(datetime.datetime.now().strftime('%x'))

# OUTPUT: 09/23/24

'''10) %X '''
# --------------------

# import datetime
# print(datetime.datetime.now().strftime('%X'))

# OUTPUT: 12:47:16

# .................................................

# (2) math
# ----------------------
# methods of math:

'''1) ceil() - rounds a decimal number to greater value'''
# --------------------------------------------------

# import math
# print(math.ceil(12.3))

# OUTPUT: 13

'''2) floor() - rounds a decimal number to lower value'''
# ---------------------------------------------------

# import math
# print(math.floor(12.3))

# OUTPUT: 12

'''3) factorial() - finds factorial of anumber '''
# ----------------------------------------

# import math
# print(math.factorial(5))

# OUTPUT: 120

'''4) sqrt()'''
# ------------------------

# import math
# print(math.sqrt(9))

# OUTPUT: 3.0
