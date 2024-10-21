a="chetu india private".split()
for i in a:
    for j in range(len(i)):
        if j==0:
            print(i[j].upper(),end="")
        elif j==len(i)-1:
            print(i[j].upper(),end="")
        else:
            print(i[j].lower(),end="")
    print(end=" ")