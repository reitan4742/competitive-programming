N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

tmp = 0
ans = -1
A = set(C)
if T in C:
    for i in range(N):
        if C[i] == T and tmp < R[i]:
            tmp = R[i]
            ans = i
else:
    c = C[0]
    for i in range(N):
        if C[i] == c and tmp < R[i]:
            tmp = R[i]
            ans = i
print(ans+1)
