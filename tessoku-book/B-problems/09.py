N = int(input())
P = [[0 for _ in range(1501)] for _ in range(1501)]
for _ in range(N):
  a, b, c, d = map(int, input().split())
  P[a][b] += 1
  P[a][d] -= 1
  P[c][b] -= 1
  P[c][d] += 1

for i in range(0, 1501):
  for j in range(1, 1501):
    P[i][j] += P[i][j-1]

for j in range(0, 1501):
  for i in range(1, 1501):
    P[i][j] += P[i-1][j]

count = 0
for i in range(1500):
  for j in range(1500):
    if P[i][j] > 0:
      count += 1

print(count)