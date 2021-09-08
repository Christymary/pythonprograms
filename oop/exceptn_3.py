#eligible fpr vaccination

age=int(input("enter age"))
if age>=18:
    print("eligible for vaccination")
else:
    raise Exception("not eligible")