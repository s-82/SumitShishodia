# 2) operator overloading
# 1)binary operation
# class Test:
#     def __init__(self,val):
#         self.val=val
#     def __add__(obj1,obj2):
#         return obj1.val+obj2.val
#     def __sub__(obj1,obj2):
#         return obj1.val-obj2.val
#     def __mul__(obj1,obj2):
#         return obj1.val*obj2.val
#     def __truediv__(obj1,obj2):
#         return obj1.val//obj2.val
#     def __floordiv__(obj1,obj2):
#         return obj1.val//obj2.val
#     def __lt__(self,other):
#         return self.val<other.val
# t1=Test(4)
# t2=Test(2)
# print(t1+t2)
# print(t1-t2)
# print(t1*t2)
# print(t1/t2)
# print(t1//t2)
# print(t1<t2)

# 2) comparison operation(
class Test1:
    def __init__(self,val):
        self.val=val
    def __nq__(obj1,obj2):
        return obj1.val != obj2.val
t1=Test1(23)
t2=Test1(43)
print(t1!=t2)
