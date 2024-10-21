a,b=0,1
print(a,b, end=" ")
for i in range(10):
    z=a+b
    print(z,end=" ")
    a=b
    b=z
