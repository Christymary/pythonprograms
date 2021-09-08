
#sum of pairs


lst=[2,3,4,5]
total=6
for i in lst:
    for j in range(i+1):
        if((i+j)==6):
            print(i,j)