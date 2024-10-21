a={1:2,2:3,3:4,5:1}
sum=sorted(a.values())
ans={}
for i in sum:
    for key,values in a.items():
        if values==i:
            ans[key]=i
            break
print(ans)