N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

E = set()
F = set()
for i in range(N):
    for j in range(N):
        tmp1 = A[i] + B[j]
        tmp2 = C[i] + D[j]
        if not tmp1 in E:
            E.add(tmp1)
        if not tmp2 in F:
            F.add(tmp2)

flag = False
for e in E:
    if K - e in F:
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")