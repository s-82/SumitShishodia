# heirarchical inheritance
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
obj.c()