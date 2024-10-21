a=[1,2,3,[1,2,3,[1,2,3],23],12]
b=[]
for i in a:
    if type(i)==list:
        for j in i:
            b.append(j)
    else:
        b.append(i)
c=b.sort()
print(c)