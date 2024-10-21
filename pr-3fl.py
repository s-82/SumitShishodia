#swallow copy
# import copy
# a=[1,2,3,[4,5,6]]
# b=copy.copy(a)
# a[-1][0]="sumit"
# print(a)
# print(b)

#deep copy
import copy
a=[1,2,3,[4,5,6]]
b=copy.deepcopy(a)
a[-1][0]="sumit"
print(a)
print(b)