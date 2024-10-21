class Car:
    def __init__(self,company,model,year):
        self.com=company
        self.mod=model
        self.yr=year
    def display(self):
        print(self.com,self.mod,self.yr)
obj=Car("maruti","zxi",2022)
obj.display()           