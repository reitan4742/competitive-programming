N, K = map(int, input().split())
A = list(map(int, input().split()))

def check(x):
  total = 0
  for i in range(N):
    total += x // A[i]
  if total >= K:
    return True
  else:
    return False

l = 1
r = 10**9
while l < r:
  m = (l+r)//2
  ans = check(m)
  if ans:
    r = m
  else:
    l = m + 1

print(l)