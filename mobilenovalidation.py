'''Phone number validation program:'''
# ----------------------------------------

import re 
a='9876543210'
if len(a)==10 and re.search('[6-9].{9}',a) and a.isdigit():
    print("valid")
else:
    print("invalid")
    
# output: valid