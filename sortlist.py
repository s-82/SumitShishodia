a=[12,11,2,3,4,5]

for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]>=a[j]:
            a[i],a[j]=a[j],a[i]

    
print(a)