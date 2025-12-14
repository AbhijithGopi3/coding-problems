a=[1,2,6,4,9]
first=second=-1
for i in a:
    if i>first:
        second=first
        first=i
    elif i>second and i!=first:
        second=i
print(second)