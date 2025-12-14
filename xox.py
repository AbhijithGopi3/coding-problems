n=int(input("enter the number: "))
m=int(input("enter the number: "))
while n<=m:
    s=0
    num=n
    while num>0:
        rem=num%10
        s=s*10+rem
        num=num//10
    if s==n:
        print(n)
    n=n+1

    
