a={'a':'apple','b':'boy','c':'car'}
l1=[]
l2=[]
c={}
for x,y in a.items():
    l1.append(x) or l2.append(y)

for l2,l1 in zip(l1,l2):
    c[l1]=l2
print(c)