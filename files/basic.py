#f1=open('sample','r')
#print(f1)
#for i in f1:
 #   print(i)

#f1=open('abc','w')
#f1.write("hello")

f1=open('abc','r')
f2=open('abccopy','w')
for i in f1:
    f2.write(i)
