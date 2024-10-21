class cal:
    def add(self,a,b):
        self.n=a
        self.n1=b
        self.c=self.n+self.n1
    def msg(self):
        print("addition",self.n1)
d=cal()
d.add(33,44)
d.msg()
print(d.c)