N, Q = map(int, input().split())
A = list(map(int, input().split()))
lr = [map(int, input().split()) for _ in range(Q)]
l, r = [list(i) for i in zip(*lr)]
S = [0]
for i in range(N):
  S.append(A[i]+S[i])

for i in range(Q):
  if l[i] == 1:
    print(S[r[i]])
  else:
    print(S[r[i]] - S[l[i]-1])