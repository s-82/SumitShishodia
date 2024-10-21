class Abc:
    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.second_name=lname
        self.age=age
    def display(self):
        print(f"your firstname is{self.first_name} and last name is{self.second_name} and age is{self.age}")
d=Abc('SUMIT','SHISHODIA',22)
d.display()  
