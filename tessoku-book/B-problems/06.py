N = int(input())
A = list(map(int, input().split()))
Q = int(input())
lr = [map(int, input().split()) for _ in range(Q)]
l, r = [list(i) for i in zip(*lr)]
S = [0]
for i in range(N):
  S.append(A[i]+S[i])

for i in range(Q):
  length = r[i] - l[i] + 1
  cnt = S[r[i]] - S[l[i]-1]
  if length%2 == 0 and cnt == length//2:
    print("draw")
  elif cnt > length//2:
    print("win")
  else:
    print("lose")
