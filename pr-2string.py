a="geeks for geeks"
b="learning geeks for geeks"
a1=a.split()
b1=b.split()
for i in a1:
    if i not in b1:
        print(i)
for i in b1:
    if i not in a1:
        print(i)