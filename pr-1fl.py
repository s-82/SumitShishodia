f1=open("testing.txt","a+")
user=input("enter name:")
password=input("enter password:")
store=user+password+" "
f1.write(store)
f1.seek(0)
print(f1.read())
f1.close()


