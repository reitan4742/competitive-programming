N = int(input())

l = 0.0
r = 100.0
for i in range(20):
  x = (l+r) / 2.0
  ans = x*x*x + x
  if ans > N:
    r = x
  else:
    l = x

print(x)