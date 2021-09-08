lst1=[1,2,3,4,5,6,6,7,8,9,11,22,33,44,55,66,77,88,99]
def search(lst1):

    element = int(input("enter the element to check"))
    flag=0
    for i in lst1:
             if i==element:
                 flag=1
                 break
    if flag==0:
        print("not found")
    else:
        print("found")


search(lst1)


