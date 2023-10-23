D = int(input())
N = int(input())
lr = [map(int, input().split()) for _ in range(N)]
L, R = [list(i) for i in zip(*lr)]
A = [0 for _ in range(D+1)]

for l, r in zip(L, R):
  A[l-1] += 1
  A[r] -= 1

num = 0
for i in range(D):
  num += A[i]
  print(num)
