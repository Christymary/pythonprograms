f1=open('abc','r')
f2=open('aabccopy','w')
for i in f1:
    f2.write(i)
