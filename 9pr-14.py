class Test:
    def __init__(self,a):
        self.val=a
    def __iadd__(self,other):
        self.val+=other.val
        return self
t1=Test(30)
t2=Test(20)
t1+=t2
print(t1.val)