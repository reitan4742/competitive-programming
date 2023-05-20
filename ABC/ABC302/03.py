import itertools
N, M = map(int, input().split())
S = []
l = []
for i in range(N):
    S.append(input())
    l.append(i)

l = list(itertools.permutations(l))

flag = False
for i in range(len(l)):
    for j in range(N-1):
        cnt = 0
        for k in range(M):
            if not S[l[i][j]][k] == S[l[i][j+1]][k]:
                cnt += 1
        if not cnt == 1:
            break
        if cnt == 1 and j == N - 2:
            flag = True

if flag:
    print("Yes")
else:
    print("No")
