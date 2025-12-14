a=input("enter the string: ")
result=""
vw="aeiouAEIOU"
for i in a:
    if i not in vw:
        result=result+i
print(result)
