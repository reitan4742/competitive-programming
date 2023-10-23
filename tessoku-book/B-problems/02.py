A, B = map(int, input().split())
flag ="No"
for i in range(A, B+1):
  if 100%i == 0:
    flag = "Yes"
    break

print(flag)
