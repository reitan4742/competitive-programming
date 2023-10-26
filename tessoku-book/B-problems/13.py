N, K = map(int, input().split())
A = list(map(int, input().split()))

count = 0
for i in range(N):
    tmp = A[i]
    if tmp <= K:
        count += 1
    for j in range(i+1,N):
        tmp += A[j]
        if tmp <= K:
            count += 1
        else:
            break

print(count)