class Test:
    def __init__(self,val):
        self.val=val
    def __add__(obj1,obj2):
        return obj1.val+obj2.val
t1=(Test(20))
t2=(Test(23))
print(t1+t2)