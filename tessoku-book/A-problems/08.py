H, W = map(int, input().split())
X = []
for i in range(H):
  tmp = list(map(int, input().split()))
  X.append(tmp)

S = [[0 for i in range(W)] for j in range(H)]
for i in range(H):
  for j in range(W):
    if j == 0:
      S[i][j] += X[i][j]
    else:
      S[i][j] += X[i][j] + S[i][j-1]

for i in range(W):
  for j in range(1,H):
    S[j][i] += S[j-1][i]

Q = int(input())
for i in range(Q):
  A, B, C, D = map(int, input().split())
  if A == 1 and B == 1:
    ans = S[C-1][D-1]
  elif A == 1:
    ans = S[C-1][D-1] - S[C-1][B-2]
  elif B == 1:
    ans = S[C-1][D-1] - S[A-2][D-1]
  else:
    ans = S[C-1][D-1] - S[A-2][D-1] - S[C-1][B-2] + S[A-2][B-2]
  print(ans)