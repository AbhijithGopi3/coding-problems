r=[4,1,6,2]
first=second=-1
for i in r:
    if i>first:
        second=first
        first=i
    elif i>second and i!=first:
        second=i
print(second)
