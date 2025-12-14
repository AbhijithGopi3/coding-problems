n = int(input("enter the starting number: "))
m = int(input("enter the ending number: "))

while n <= m:
    s = 0
    num = n
    digits = len(str(n))
    while num > 0:
        rem = num % 10
        s = s + (rem ** digits)
        num = num // 10
    if s == n:
        print(n)
    n = n + 1
