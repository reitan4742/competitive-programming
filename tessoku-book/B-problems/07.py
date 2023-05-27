T = int(input())
N = int(input())
S = [0 for _ in range(T+1)]
for i in range(N):
  l, r = map(int, input().split())
  S[l] += 1
  S[r] -= 1

cnt = 0
for i in range(T):
  cnt += S[i]
  print(cnt)