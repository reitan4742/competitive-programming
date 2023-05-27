D = int(input())
N = int(input())
S = [0 for _ in range(D)]
for i in range(N):
  l, r = map(int, input().split())
  S[l-1] += 1
  if not r == D:
    S[r] -= 1

cnt = 0
for i in S:
  cnt += i
  print(cnt)