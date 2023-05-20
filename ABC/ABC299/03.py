N = int(input())
S = input()

max_count = 0
count = 0
flag = False
for i in range(N):
    if S[i] == "-":
        if not flag:
            flag = True
        else:
            if max_count < count:
                max_count = count
            count = 0
    else:
        if flag:
            count += 1
if max_count < count:
    max_count = count

count = 0
flag = False
for i in reversed(range(N)):
    if S[i] == "-":
        if not flag:
            flag = True
        else:
            if max_count < count:
                max_count = count
            count = 0
    else:
        if flag:
            count += 1
if max_count < count:
    max_count = count

if max_count == 0:
    print(-1)
else:
    print(max_count)
