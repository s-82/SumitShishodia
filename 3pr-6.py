from abc import ABC,abstractmethod
class Abs(ABC):
    @abstractmethod
    def display():
        pass
class Derived(Abs):
    def display(self):
        print(f"this is a print method")
obj=Derived()
obj.display()