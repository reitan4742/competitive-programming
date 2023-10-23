N = int(input())
A = list(map(int, input().split()))
Q = int(input())
lr = [map(int, input().split()) for _ in range(Q)]
L, R = [list(i) for i in zip(*lr)]

B = [0]
tmp = 0
for a in A:
  tmp += a
  B.append(tmp)

for l, r in zip(L, R):
  pull = r - l + 1
  win = B[r] - B[l-1]
  if win > pull - win:
    print("win")
  elif win < pull - win:
    print("lose")
  else:
    print("draw")
