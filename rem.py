a=input("enter the string: ")
result=""
for i in range(len(a)):
    if i%2==0:
        result=result+a[i]
print(result)
