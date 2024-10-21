a=['hello','abc','hero','god','shyam','some','aam','get']
a.sort()
b=[]
for i in a:
    if(i[0][0] not in b):
        b.append(i[0][0])

c={}
for i in b:
    var=[]
    for j in a:
        if(i==j[0]):
            var.append(j)
    c[i]=var
print(c)