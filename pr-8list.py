a=input("enter number or word")
a=str(a)
if a==a[::-1]:
    print("palindrome")
else:
    print("not palindrome")