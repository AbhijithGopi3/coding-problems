n=int(input("enter the number:"))
m=int(input("enter the number:"))
s=0
for i in range(n,m+1):
        rem=i%10
        s=rem**3+s
        i=i//10
        if s==n:
            print(n)
    
        
