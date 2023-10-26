N, K = map(int, input().split())
A = list(map(int, input().split()))
B = []
C = []
for i in range(N//2):
    B.append(A[i])
for i in range(N//2,N):
    C.append(A[i])

D = set()
E = set()
for i in range(2**(len(B))):
    count = 0
    for j in range(len(B)):
        if ((i >> j) & 1):
            count += B[j]
    if not count in D:
        D.add(count)

for i in range(2**(len(C))):
    count = 0
    for j in range(len(C)):
        if ((i >> j) & 1):
            count += C[j]
    if not count in E:
        E.add(count)

flag = False
for d in D:
    if K - d in E:
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")