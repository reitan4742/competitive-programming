N = int(input())
S = input()

count = 0
flag = False
for s in S:
    if s == "|":
        count += 1
    if count == 1 and s == "*":
        flag = True
if flag:
    print("in")
else:
    print("out")
