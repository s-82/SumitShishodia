count=1
for x in range(1,6):
    for y in range(5,0,-1):
        if y>x:
            print(" ",end=" ")
        else:
            print(count,end=" ")
            count+=1
    print()