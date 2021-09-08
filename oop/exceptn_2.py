#division less by greater

a=int(input("enter"))
b=int(input("enter"))
if b>a:
    raise Exception("second number is greater")
else:
    print(a/b)