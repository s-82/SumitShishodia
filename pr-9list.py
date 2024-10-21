a=int(input("enter the num"))
count=0
for i in range(2,a//2+1):
    if a%i==0:
        count+=1
        break
if count==0:
    print("prime")
else:
    print("not prime")