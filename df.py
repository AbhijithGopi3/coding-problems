n=int(input("enter the number"))
s=0
num=n
while num>0:
    rem=num%10
    s=s*10+rem
    num=num//10
    n=n+1
print(s)
    
    
