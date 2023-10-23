H, W = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(H)]

Y = [list(0 for _ in range(W+1)) for _ in range(H+1)]

for i in range(H):
  for j in range(W):
    Y[i+1][j+1] = Y[i+1][j] + X[i][j]

for i in range(W):
  for j in range(H):
    Y[j+1][i+1] += Y[j][i+1]

Q = int(input())
for i in range(Q):
  a, b, c, d = map(int, input().split())
  print(Y[c][d] + Y[a-1][b-1] - Y[c][b-1] - Y[a-1][d])
