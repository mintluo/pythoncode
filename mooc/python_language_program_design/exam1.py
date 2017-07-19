string = input()
list=string.split(",")
for i in list:
    k=i.strip()
    for j in list:
        n=j.strip()
        if k!=n:
            print(k+n)