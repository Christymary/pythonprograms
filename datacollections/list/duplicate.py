lst=[1,2,4,5,7,48,2,8,9,3,5]
b=[]
for i in lst:
    if i not in b:
        b.append(i)
    else:
        print(i)
