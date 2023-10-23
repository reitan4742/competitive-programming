n = int(input())
wx = [map(int, input().split()) for _ in range(n)]
w, x = [list(i) for i in zip(*wx)]
num = -1
for i in range(24):
  tmp = 0
  for j in range(n):
    time = (i+x[j]) % 24
    if 9 <= time < 18:
      tmp += w[j]
  if num < tmp:
    num = tmp

print(num)