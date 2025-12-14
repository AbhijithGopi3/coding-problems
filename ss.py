s=list(map(int,input("enter the elements: ").split()))
first=second=-1
for i in s:
    if i>first:
        second=first
        first=i
    elif i>second and i!=first:
        second=i
        print(second)
