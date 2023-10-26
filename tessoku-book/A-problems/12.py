N, K = map(int, input().split())
A = list(map(int, input().split()))

def check(x):
    sum_x = 0
    for a in A:
        sum_x += x // a
    if sum_x >= K:
        return True
    else:
        return False

L = 1
R = 10**9
while L < R:
    M = (L + R)//2
    if check(M):
        R = M
    else:
        L = M + 1

print(L)