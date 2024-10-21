# hollow diamond pattern
n=5
for i in range(1,n):
    for j in range(1,2*n):
        if(j==(n-i+1) or j==(n+i-1) or (i==n and j%2!=0)):
            print("*",end="")
        else:
            print(" ",end="")
    print()


n=5
for i in range(n-1,0,-1):
    for j in range(1,2*n):
        if(j==(n-i+1) or j==(n+i-1) or (i==n and j%2!=0)):
            print("*",end="")
        else:
            print(" ",end="")
    print()