N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = list()
dp = [None for _ in range(N)]
dp[0] = 0
dp[1] = A[0]
for i in range(2,N):
    dp[i] = min(dp[i-1] + A[i-1], dp[i-2] + B[i-2])

j = N-1
while True:
    ans.append(j+1)
    if j == 0:
        break

    if dp[j] == dp[j-1] + A[j-1]:
        j -= 1
    else:
        j -= 2

print(len(ans))
ans.sort()
print(*ans)