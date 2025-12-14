n=int(input("enter the number: "))
m=int(input("enter the number: "))
prime=True
if n<=1:
    prime=False
else:
    prime=True
    for i in range(n,m):
        if m%i==0:
            prime=False
            break
    if prime:
        print(m)
    else:
        print("it is not a prime number")
