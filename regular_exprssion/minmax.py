#minimum length 8 maximum length 15 --string(except numbers)

import re

n=input("enter")
x="([\D]{8,15})"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
