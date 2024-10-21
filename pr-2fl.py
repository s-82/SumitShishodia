file=open("cred.txt","w+")
user=input("enter name")
file.write(user)
count=0
file.seek(0)
f1=file.read().split()
name=input("enter anything inside a user")
for i in f1:
    if name.count(i):
        count+=1
print(count)

