a={1,2,3,4,5,6,'vivek','sumit'}
b=list(a)
mid=len(b)//2
dic={}
for i in range(mid):
    dic[b[i]]=b[mid+i]
print(dic)