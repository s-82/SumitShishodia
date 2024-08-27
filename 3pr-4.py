def wrapper(function):
    def inner():
        print(f"good morning")
        function()
        print(f"hAVE A GOOD ")

    return inner
@wrapper
def display():
    print("this is a function")

display()