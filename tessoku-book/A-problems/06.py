N, Q = map(int, input().split())
A = list(map(int, input().split()))
lr = [map(int, input().split()) for _ in range(Q)]
L, R = [list(i) for i in zip(*lr)]

B = [0]
tmp = 0
for a in A:
  tmp += a
  B.append(tmp)

for l, r in zip(L, R):
  print(B[r] - B[l-1])
