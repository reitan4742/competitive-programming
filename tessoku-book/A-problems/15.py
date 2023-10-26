import bisect
N = int(input())
A = list(map(int, input().split()))
X = list(set(A))
X.sort()
B = [0 for _ in range(N)]
for i in range(N):
    B[i] = bisect.bisect_right(X, A[i])

print(*B)
