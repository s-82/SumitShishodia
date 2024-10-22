# arr=[1,2,3,4,5,6,7,8,10]
# n=len(arr)
# total=((n+1)*(n+2))//2
# summ=sum(arr)
# print(total-summ)

def miss(arr):
    n=len(arr)
    total=((n+1)*(n+2))//2
    return total-sum(arr)
b=[1,2,3,4,5,6,7,8,10]
print(miss(b))


