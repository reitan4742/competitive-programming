N, M, H, K = map(int, input().split())
S = input()
xy = [map(int, input().split()) for _ in range(M)]
x, y = [list(i) for i in zip(*xy)]
l = []
for i in range(M):
  l.append(str(x[i])+str(y[i]))
l = set(l)
now_x = 0
now_y = 0
flag = True
for s in S:
  H -= 1
  if H < 0:
    flag = False
    break
  if s == "R":
    now_x += 1
    tmp = str(now_x)+str(now_y)
    if H < K and tmp in l:
      H = K
      l.remove(tmp)
  if s == "L":
    now_x -= 1
    tmp = str(now_x)+str(now_y)
    if H < K and tmp in l:
      H = K
      l.remove(tmp)
  if s == "U":
    now_y += 1
    tmp = str(now_x)+str(now_y)
    if H < K and tmp in l:
      H = K
      l.remove(tmp)
  if s == "D":
    now_y -= 1
    tmp = str(now_x)+str(now_y)
    if H < K and tmp in l:
      H = K
      l.remove(tmp)

if flag:
  print("Yes")
else:
  print("No")