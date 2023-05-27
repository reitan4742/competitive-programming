N = int(input())
x = input()
y = input()
flag = True
for i in range(N):
  if (x[i] == "1" and y[i] == "l") or (x[i] == "l" and y[i] == "1"):
    pass
  elif (x[i] =="0" and y[i] == "o") or (x[i] == "o" and y[i] == "0"):
    pass
  elif x[i] == y[i]:
    pass
  else:
    flag = False

if flag:
  print("Yes")
else:
  print("No")