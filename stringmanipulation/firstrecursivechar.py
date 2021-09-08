str=input("Enter the string")
k=""
for i in str:
    if i not in k:
        k=k+i
    else:
        print(i)
        break




