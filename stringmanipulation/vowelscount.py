str= input("Enter a String:")
vow='aeiou'
count=0
for i in str:
    if i in vow:
        count=count+1
print("The count of vowels in the string is",count)
