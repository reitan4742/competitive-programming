N, A, B = map(int, input().split())
ans = A + B
C = list(map(int, input().split()))

for i in range(len(C)):
    if ans == C[i]:
        print(i+1)
        break
