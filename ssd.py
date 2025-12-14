a=int(input("enter the number"))
prime=True
if a>1:
        prime=True
        for x in range(2,int(a**0.5)+1):
            if a%x==0:
                prime=False
                break
        if prime:
            print("it is prime number")
        else:
            print("it is not a prime number")
