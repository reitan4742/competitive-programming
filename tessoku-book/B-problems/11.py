import bisect
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
X = []
for i in range(Q):
  tmp = int(input())
  X.append(tmp)

A.sort()
for i in range(Q):
  print(bisect.bisect_left(A, X[i]))