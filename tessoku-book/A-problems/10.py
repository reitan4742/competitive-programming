N = int(input())
A = list(map(int, input().split()))
D = int(input())
ld = [map(int, input().split()) for _ in range(D)]
l, d = [list(i) for i in zip(*ld)]
P = [0,A[0]]
Q = [0,A[-1]]
for i in range(2,N):
  P.append(max(P[i-1], A[i-1]))
  Q.append(max(Q[i-1], A[-i]))

for i in range(D):
  print(max(P[l[i]-1], Q[N-d[i]]))