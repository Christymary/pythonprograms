#division by zero error

no1=int(input("enter"))
no2=int(input("enter"))
try:
    print(no1/no2)
except Exception as a:
    print(a.args)