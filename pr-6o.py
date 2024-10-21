class samsung:
    cl=20
    def dis(self,val):
        self.display=val
    @classmethod
    def change(self,val):
        self.cl=val
    @staticmethod
    def greet():         
        print("hello")
sohan=samsung()       
amit=samsung()        
amit.change(4)
print(sohan.cl)
print(amit.cl)  
print(amit.cl)  
amit.greet()