# n=int(input("enter the number"))
# alph=65
# for i in range(0,n):
#     print(" "* (n-i),end=" ")
#     for j in range(0,i+1):
#         print(chr(alph),end=" ")
#         alph+=1
#     alph=65
#     print()
        

n=4
for i in range(1,n+1):
    print(' '*(n-i),"*"*(2*i-1))
for i in range((n-1),0,-1):
    print(" "*(n-i),"*"*(2*i-1))