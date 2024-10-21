#duplicate value print from integer list
l=[1,1,2,3,4,5,6,6]
temp=[]
for i in l:
    if l.count(i)>1:
        if i not in temp:
            temp.append(i)
print(temp)