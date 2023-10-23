T = int(input())
N = int(input())
lr = [map(int, input().split()) for _ in range(N)]
L, R = [list(i) for i in zip(*lr)]
A = [0 for _ in range(T+1)]
for l, r in zip(L, R):
  A[l] += 1
  A[r] -= 1

B = []
tmp = 0
for i in range(T+1):
  tmp += A[i]
  B.append(tmp)

for i in range(T):
  print(B[i])