# 1)method overloading
# class Test():
#     def add(self):
#         print("no arg")
#     def add(self,a):
#         print("1 arg")
#     def add(self,a,b):
#         print("2 arg")
#     def add(self,a,b,c):
#         print("3 arg")
# obj=Test()
# obj.add(2)

# for above problem we use multiple dispatch
from multipledispatch import dispatch
class Test():
    @dispatch()
    def add(self):
        print("no arg")
    @dispatch(int)
    def add(self,a):
        print("int")
    @dispatch(float)
    def add(self,a):
        print("float")
    @dispatch(str)
    def add(self,a):
        print("string")
obj=Test()
obj.add("sum")