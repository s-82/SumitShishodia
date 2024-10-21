class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
class B(A):
    def add(self):
        self.c=self.a+self.b
        print(f"addition of two number: {self.c}")
class C(B):
    def square(self):
        self.d=self.c*self.c
        print(f"addition of two number is {self.d}")
obj=C(3,3)
obj.add()
obj.square()
