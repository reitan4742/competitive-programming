import bisect
N, K = map(int, input().split())
A = list(map(int, input().split()))

count = 0
for i in range(N):
    tmp = bisect.bisect_right(A,A[i]+K) - i - 1
    count += tmp

print(count)
