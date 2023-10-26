N, X = map(int, input().split())
A = list(map(int, input().split()))

def search(x):
    L = 0
    R = N
    while L <= R:
        M = (L + R)//2
        if X < A[M]:
            R = M - 1
        elif X > A[M]:
            L = M + 1
        else:
            return M

print(search(X)+1)
