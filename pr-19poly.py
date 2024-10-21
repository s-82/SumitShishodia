# assignment opertor
# iadd
# class Test:
#     def __init__(self,a):
#         self.val=a
#     def __iadd__(self,other):
#         self.val+=other.val
#         return self
# t1=Test(30)
# t2=Test(40)
# t1+=t2
# print(t1.val)                                            
  
# isub
# class Test:     
#     def __init__(self,a):
#         self.val=a
#     def __isub__(self,other):
#         self.val-=other.val
#         return self
# t1=Test(30)
# t2=Test(40)
# t1-=t2
# print(t1.val)                                            

class Test:
    def __init__(self,a):
        self.val=a
    def __ipow__(obj1,obj2):
        obj1.val**=obj2.val
        return obj1
t1=Test(2)
t2=Test(2)
t1**=t2
print(t1.val)

