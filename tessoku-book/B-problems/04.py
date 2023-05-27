N = input()
i = len(N) - 1
ans = 0
for n in N:
  ans += int(n)*2**i
  i -= 1
print(ans)