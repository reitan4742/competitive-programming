N, S = map(int, input().split())
A = list(map(int, input().split()))
dp = [[False for _ in range(S+1)] for _ in range(N+1)]
dp[0][0] = True
for i in range(1,N+1):
    for j in range(S+1):
        if dp[i-1][j]:
            dp[i][j] = True
        elif j >= A[i-1]:
            if dp[i-1][j - A[i-1]]:
                dp[i][j] = True

if dp[-1][-1]:
    ans = []
    j = S
    for i in reversed(range(1,N+1)):
        if dp[i-1][j]:
            j -= 0
        else:
            ans.append(i)
            j = j - A[i-1]
    print(len(ans))
    ans.sort()
    print(*ans)
else:
    print(-1)