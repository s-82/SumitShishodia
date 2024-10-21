# for x in range(5):
#     for y in range(x):
#         if y%2==0:
#             print("1",end=" ")
#         else:
#             print("2",end=" ")
#     print()

count=1
for x in range(1,6):
    for y in range(5,0,-1):
        if y>x:
            print(" ",end="")
        else:
            print(count,end="")
            count=count+1
    print()