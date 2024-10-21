#snake case to pascal case
name=input("enter the name")
for i in range(len(name)):
    if i==0:
        print(name[i].upper(),end='')
    elif (name[i]=='_'):
        continue
    elif (name[i-1]=='_'):
        print(name[i].upper(),end='')
    else:
        print(name[i],end='')
