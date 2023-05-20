N = int(input())
l = 1
r = N
while True:
    index = (l+r)//2
    print("?"+str(index))
    re = int(input())
    if re == 0:
        l = index
    else:
        r = index
    if r - l == 1:
        print("!"+str(l))
        break
