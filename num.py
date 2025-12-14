num=int(input("enter the number: "))
s=0
n=num
while num>0:
    rem=num%10
    s=rem**3+s
    num=num//10
if s==n:
    print("it is armstrong number")
else:
    print("moonjiko")
