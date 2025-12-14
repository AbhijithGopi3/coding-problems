a=input("enter the string: ")
palindrome=True
for i in range(len(a)//2):
    if a[i]!=a[len(a)-1-i]:
        palindrome=False
if palindrome:
    print("it is apalindrome")
else:
    print("it is not a palindrome")
