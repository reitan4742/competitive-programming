N = int(input())
A = list(map(int, input().split()))
D = int(input())
lr = [map(int, input().split()) for _ in range(D)]
L, R = [list(i) for i in zip(*lr)]
left_max = [0]
right_max = [0]

tmp = 0
for a in A:
    if tmp < a:
        tmp = a
    left_max.append(tmp)

tmp = 0
for a in reversed(A):
    if tmp < a:
        tmp = a
    right_max.append(tmp)

for l, r in zip(L, R):
    print(max(left_max[l-1],right_max[N - r]))
