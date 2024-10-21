# class Car:
#     def __init__(self,mil,engine):
#         self.mil=mil
#         self.eng=engine
#     def display(self):
#         print(self.mil,self.eng)
# class Bike(Car):
#     def __init__(self,mil,engine,wheel):
#         super().__init__(mil,engine)
#         self.wheel=wheel
# class Bus(Bike):
#     def __init__(self,mil,engine,wheel,capacity):
#         super().__init__(mil,engine,wheel)
#         self.capacity=capacity
# obj=Bus("45km","250cc","diamond cut",50)
# print(obj.capacity)


class A:
    def test(self):
        print("A")
class B:
    def test(self):
        print("B")

class C(B,A):
    pass
obj=C()
print(C.__mro__)