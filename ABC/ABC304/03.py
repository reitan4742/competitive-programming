import queue

N, D = map(int, input().split())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]
ans = [False for i in range(N)]
ans[0] = True
rel = [[] for i in range(N)]

for i in range(N):
  for j in range(i+1,N):
    if ((x[i]-x[j])**2 + (y[i]-y[j])**2)**0.5 <= D:
      rel[i].append(j)
      rel[j].append(i)

q = queue.Queue()
for i in rel[0]:
  ans[i] = True
  q.put(i)

while not q.empty():
  p = q.get()
  for i in rel[p]:
    if not ans[i]:
      q.put(i)
      ans[i] = True

for s in ans:
  if s:
    print("Yes")
  else:
    print("No")