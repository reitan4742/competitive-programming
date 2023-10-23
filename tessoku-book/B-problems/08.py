N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
X, Y = [list(i) for i in zip(*xy)]
P = [[0 for _ in range(1501)] for _ in range(1501)]
for x, y in zip(X, Y):
  P[x][y] += 1

S = [[0 for _ in range(1501)] for _ in range(1501)]
for y in range(1,1501):
  for x in range(1,1501):
    S[x][y] = S[x-1][y] + P[x][y]

for x in range(1,1501):
  for y in range(1,1501):
    S[x][y] += S[x][y-1]

Q = int(input())
for _ in range(Q):
  a, b, c, d = map(int, input().split())
  print(S[a-1][b-1] + S[c][d] - S[a-1][d] - S[c][b-1])
