N = int(input())
C = [[0 for i in range(1501)] for i in range(1501)]

for i in range(N):
  x, y = map(int, input().split())
  C[x][y] += 1
  
S = [[0 for i in range(1501)] for j in range(1501)]
for x in range(1,1501):
  for y in range(1,1501):
    S[x][y] += C[x][y] + S[x][y-1]

for y in range(1, 1501):
  for x in range(1, 1501):
    S[x][y] += S[x-1][y]

Q = int(input())
for i in range(Q):
  a, b, c, d = map(int, input().split())
  ans = S[c][d] - S[a-1][d] - S[c][b-1] + S[a-1][b-1]
  print(ans)