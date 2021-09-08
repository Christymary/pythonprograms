lst=[8,89,6,457,36,87,]

def bsearch():
    lst.sort()
    k=int(input("Enter the number to search"))
    flag=0
    low=0
    high=len(lst)-1
    while low <= high:
        mid = (low+high) // 2 #flow division is done to avoid fraction so that we get middle value as integer

        if k > lst[mid]:
            low = mid+1
        elif k < lst[mid]:
            high = mid-1
        elif k == lst[mid]:
            flag=1
            break
    if flag==1:
        print("found")
    else:
        print("not found")
bsearch()