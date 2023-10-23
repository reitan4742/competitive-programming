n, x = map(int, input().split())
A = list(map(int, input().split()))
flag = "No"
for a in A:
  if a == x:
    flag = "Yes"
    break

print(flag)