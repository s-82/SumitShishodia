# class sports:
#     def run(self):
#         print("runing")
#         print(id(self))
# ram=sports() 
# shyam=sports()
# mohan=sports()
# sports.run(ram)
# print(id(ram))

# x= 10       
# def abc():
#     x=5
#     def xyz():
#         nonlocal x
#         print(x)
#     xyz()
# abc()

# x=10
# def abc():
#     x=5
#     def xyz():
#         global x
#         x+=1
#         print(x)       
#     xyz() 
# abc()
# print(x)

x=10
def abc():
    x=5
    def xyz():
        nonlocal x
        x+=1
        
    xyz()
    print(x)
abc()