N = int(input())
i = 0
ans = 0
while True:
    if N%2 == 1:
        ans += 1*10**i
    N //= 2
    i += 1
    if N == 0:
        break

print(str(ans).zfill(10))
