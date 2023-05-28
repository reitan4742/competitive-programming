N, M = map(int, input().split())
a = []
c = [[0 for i in range(N+1)] for j in range(N+1)]
for i in range(M):
  tmp = list(map(int, input().split()))
  a.append(tmp)

for i in range(M):
  for j in range(1,N):
    if c[a[i][j]][a[i][j-1]] == 0:
      c[a[i][j-1]][a[i][j]] = 1
      c[a[i][j]][a[i][j-1]] = 1
cnt = 0
for i in range(1,N+1):
  for j in range(i+1, N+1):
    if c[i][j] == 0:
      cnt += 1

print(cnt)