A, B = map(int, input().split())
ans = A//B
if not A%B == 0:
    ans += 1

print(ans)
