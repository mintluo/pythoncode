string = input()
ori1="abcdefghijklmnopqrstuvwxyz"
ori2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
map=ori1+ori1+ori2+ori2
result=""
for ch in string:
    if ch in map:
        j=map.find(ch)
        result=result+map[j+13]
    else:
        result=result+ch

print(result)