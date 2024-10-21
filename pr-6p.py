# hollow square pattern

# n=5
# for i in range(1,n+1):
#     for j in range(1,2*n):
#         if(j==(n-i+1) or j==(n+i-1) or (i==n and j%2!=0)):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# inverted hollow pattern
n=5
for i in range(n,0,-1):
    for j in range(1,2*n):
        if(j==(n-i+1) or j==(n+i-1) or (i==n and j%2!=0)):
            print("*",end="")
        else:
            print(" ",end="")
    print()