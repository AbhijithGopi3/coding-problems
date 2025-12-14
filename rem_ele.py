a=input("enter the string: ")
result=""
ch=input("enter the elemnt to remove: ")
for i in a:
    if i!=ch:
        result=result+i
print(result)
