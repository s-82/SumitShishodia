# polymorphism 1
# class Test:
#     def func(self):
#         print("Test")
# class Test1:
#     def func(self):
#         print("Test1")

# obj=Test()
# obj1=Test1()
# for x in obj,obj1:
#     x.func()

# polymorphism 2
class Test:
    def func(self):
        print("Test")
class Test1:
    def func(self):
        print("Test1")
def call(arg):
    arg.func()
obj=Test()
obj1=Test1()
call(obj)
call(obj1) 