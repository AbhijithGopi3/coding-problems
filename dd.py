s=list(map(int,input("enter the elements: ").split()))
su=0
for num in s:
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            su=su+num
print(su)
            
            
