def patt(n):
    num=1
    for i in range(n):
        for j in range(i):
            print(num,end=" ")
            num+=1
        print()
patt(5)