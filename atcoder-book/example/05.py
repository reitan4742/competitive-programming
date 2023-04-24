N, A, B = map(int, input().split())
sum = 0
for i in range(1, N+1):
    j = i
    tmp = 0
    while j > 0:
        tmp += j%10
        j //= 10

    # tmp = j//10000
    # j = j%10000
    # tmp += j//1000
    # j = j%1000
    # tmp += j//100
    # j = j%100
    # tmp += j//10
    # j = j%10
    # tmp += j
    if A <= tmp and tmp <= B:
        sum += i
print(sum)