age=int(input("enter age"))
if age<18:
    raise Exception("Not eligible")
else:
    print("eligible for vaccination")