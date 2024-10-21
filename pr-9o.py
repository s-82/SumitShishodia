# they are 5 types of inheritance
# 1 single inhertance
# class A:
#     def a(self):
#         print("A")
# class B(A):
#     def b(self):
#         print("B")
           
# obj=B()
# obj.b()
# obj.a()

# 2 multilevel inheritance
class A:
    def a(self):
        print("A")

class B(A):
    def b(self):
        # super().a()
        print("B")
        super().a()

class C(B):
    def c(self):
        # super().b()
        print("C")
        super().b()

obj=C()
obj.c()

