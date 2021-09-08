lst=[67,34,5,72,4,512,45,78,897,36]
s=int(input("Enter the size of list "))
for i in range(s):
    for j in range(i+1,s):
        if lst[i] > lst[j]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp

print(lst)