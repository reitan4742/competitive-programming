N = int(input())
A = list(map(int, input().split()))

count = -1
flag = True
while flag:
  count += 1
  for i in range(len(A)):
    if not A[i]%2 == 0:
      flag = False
      break
    A[i] //= 2
print(count)
