a="abcd.,%$%^"
b=".,;'$%^"
c=""
for i in a:
    if i not in b:
        c=c+i
print(c)
