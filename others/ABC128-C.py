N, M = map(int, input().split())
k = []
s = []
for i in range(M):
  tmp = list(map(int, input().split()))
  k.append(tmp[0])
  s.append(tmp[1:tmp[0]+1])
p = list(map(int, input().split()))

cnt = 0
for i in range(2**N):
  cnt_s = [0 for _ in range(M)]
  for j in range(N):
    if ((i >> j) & 1):
      for k in range(M):
        if (j + 1) in s[k]:
          cnt_s[k] += 1
  for l in range(M):
    if not cnt_s[l]%2 == p[l]:
      break
    if l == M-1:
      cnt += 1

print(cnt)