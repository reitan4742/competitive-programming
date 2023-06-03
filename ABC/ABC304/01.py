N = int(input())
S = []
A = []
for i in range(N):
  s, a = input().split()
  S.append(s)
  A.append(int(a))

min_index = A.index(min(A))

for i in range(N):
  if i + min_index >= N:
    print(S[i+min_index-N])
  else:
    print(S[i+min_index])