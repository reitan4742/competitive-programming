N = input()
ans = 0
for i in range(len(N)):
  if N[i] == "1":
    ans += 2**(len(N)-1-i)

print(ans)