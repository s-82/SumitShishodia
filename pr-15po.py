class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary
    def display(self):
        print(self.name,self.age,self.salary)

obj=Employee("aman",21,22850)
obj.display() 