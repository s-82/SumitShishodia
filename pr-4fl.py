class myerror(Exception):
    pass
num=int(input("num"))
try:
    if num==5:
        raise myerror
except myerror:
    print("press 5 number")

