yr=int(input("enter the year"))
if yr%100==0:
    if yr%400==0:
        print("leap year")
    else:
        print("not leap year")
elif yr%4==0:
    print("leap year")
else:
    print("not leap year")