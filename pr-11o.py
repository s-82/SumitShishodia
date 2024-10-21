# multiple inheritance

# class A:
#     def a(self):
#         print("A")
# class B:
#     def b(self):
#         print("B")
# class C:
#     def c(self):
#         print("C")

# class D(A,B,C):
#     def d(self):
#         super().a()
#         print("D")
# obj=D()
# obj.d()

# hybrid inheritance
class A:
    def a(self):
        print("A")
class B(A):
    def b(self):
        print("B")
class C(A):
    def c(self):
        print("C")

class D(B,C):
    def d(self):
        print("D")
obj=D()
obj.d()