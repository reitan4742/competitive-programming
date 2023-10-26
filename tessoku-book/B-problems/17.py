N = int(input())
h = list(map(int, input().split()))
dp = [None for _ in range(N)]
dp[0] = 0
dp[1] = abs(h[0] - h[1])
for i in range(2,N):
    dp[i] = min(dp[i-1] + abs(h[i] - h[i-1]), dp[i-2] + abs(h[i] - h[i-2]))

ans = []
j = N - 1
while True:
    ans.append(j+1)
    if j == 0:
        break
    if dp[j] == dp[j-1] + abs(h[j] - h[j-1]):
        j -= 1
    else:
        j -= 2

print(len(ans))
ans.sort()
print(*ans)
