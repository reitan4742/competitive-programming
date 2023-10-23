H, W, N = map(int, input().split())
P = [[0 for _ in range(W+2)] for _ in range(H+2)]
for _ in range(N):
  a, b, c, d = map(int, input().split())
  P[a][b] += 1
  P[a][d+1] -= 1
  P[c+1][b] -= 1
  P[c+1][d+1] += 1

for i in range(1,H+2):
  for j in range(1,W+2):
    P[i][j] += P[i][j-1]

for j in range(1,W+2):
  for i in range(1,H+2):
    P[i][j] += P[i-1][j]

for i in range(1,H+1):
  for j in range(1,W+1):
    print(P[i][j],end=" ")
  print()