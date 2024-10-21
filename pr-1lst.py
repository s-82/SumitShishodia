a=["Gfg is the best resource to acquire knowledege"]
b=[]
for x in a:
    c=""
    for i in x:
        if i=="G":
            c+="e"
        elif i=="e":
            c+="G"
        else:
            c+=i
    b.append(c)
print(b)