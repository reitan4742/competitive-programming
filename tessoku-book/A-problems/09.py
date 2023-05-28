H, W, N = map(int, input().split())
X = [[0 for i in range(W+2)] for j in range(H+2)]
for i in range(N):
  a, b, c, d = map(int, input().split())
  X[a][b] += 1
  X[c+1][b] -= 1
  X[a][d+1] -= 1
  X[c+1][d+1] += 1

S = [[0 for i in range(W+2)] for j in range(H+2)]
for i in range(1,H+1):
  for j in range(1,W+1):
    S[i][j] = S[i][j-1] + X[i][j]

for j in range(1,W+1):
  for i in range(1,H+1):
    S[i][j] += S[i-1][j]

for i in range(1,H+1):
  for j in range(1,W+1):
    if j >= 2:
      print(" ", end="")
    print(S[i][j], end="")
  print("")