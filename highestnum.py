a=[23,34,344,45,56]
g=a[0]
for i in range(len(a)):
    if(g<=a[i]):
        g=a[i]

print(g)