# inheritance
class Parent:
    def __init__(self,a,b):
        self.a=a
        self.b=b
class Child(Parent):
    def add(self):
        print(self.a+self.b)
c1=Child(22,33)
c1.add()