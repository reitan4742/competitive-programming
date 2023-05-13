H, W = map(int, input().split())
C = [[0 for i in range(W)] for j in range(H)]
n = [0 for i in range(min(H,W))]

for i in range(H):
    tmp = input()
    for j in range(W):
        if tmp[0] == "#":
            C[i][j] += 1

for i in range(H):
    for j in range(W):
        if C[i][j] == 1:
            d = 0
            while True:
                if i + d < H and i - d >= 0 and j + d < W and i - d >= 0:
                    if C[i+d][j+d] == 1 and C[i+d][j-d] == 1 and C[i-d][j+d] == 1 and C[i-d][j-d] == 1:
                      d += 1
                    else:
                      if d == 0:
                        break
                      else:
                        n[d] += 1
                        break
                else:
                   if d == 0:
                      break
                   else:
                      n[d] += 1
                      break

for i in range(1,len(n)):
  if i == len(n) - 1:
    print(n[i])
  else:
     print(n[i],end=" ")
