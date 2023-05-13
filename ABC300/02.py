H, W = map(int, input().split())
h1 = []
h2 = []
w1 = []
w2 = []
s1 = [[0 for i in range(W)] for j in range(H)]
s2 = [[0 for i in range(W)] for j in range(H)]
for i in range(H):
    h1.append(0)
    h2.append(0)
for i in range(W):
    w1.append(0)
    w2.append(0)

for i in range(H):
    tmp = input()
    for j in range(W):
        if tmp[j] == "#":
            h1[i] += 1
            w1[j] += 1
            s1[i][j] += 1

for i in range(H):
    tmp = input()
    for j in range(W):
        if tmp[j] == "#":
            h2[i] += 1
            w2[j] += 1
            s2[i][j] += 1

a = []
for i in range(H):
    if h1[i] == h2[0]:
        k = i
        for j in range(H):
            if not h2[j] == h1[k]:
                break
            k += 1
            if k == H:
                k = 0
            if j == H-1:
                a.append(k)

b = []
for i in range(W):
    if w1[i] == w2[0]:
        k = i
        for j in range(W):
            if not w2[j] == w1[k]:
                break
            k += 1
            if k == W:
                k = 0
            if j == W-1:
                b.append(k)

flag = False
for i in a:
    for u in b:
      for j in range(H):
        for k in range(W):
            tmp1 = (i+j)%H
            tmp2 = (u+k)%W
            if not s1[tmp1][tmp2] == s2[j][k]:
                break
            if j == H-1 and k == W-1:
                flag = True
        else:
            continue
        break

if flag:
    print("Yes")
else:
    print("No")
