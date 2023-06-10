N, X = map(int, input().split())
A = list(map(int, input().split()))

l = 0
r = N-1
while l<=r:
  m = (l+r)//2
  if X < A[m]:
    r = m - 1
  elif X > A[m]:
    l = m + 1
  else:
    print(m+1)
    break