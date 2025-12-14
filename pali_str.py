str=input("enter the string: ")
palindrome=True
l=len(str)
for i in range(l//2):
    if str[i]!=str[l-i-1]:
        palindrome=False
if palindrome:
    print("it is palindrome")
else:
    print("it is not palindrome")
