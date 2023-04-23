step = int(input())
N, X, Y = map(int, input().split())
ab = [map(int, input().split()) for _ in range(N)]
a, b = [list(i) for i in zip(*ab)]

if step == 1:
    ans = 0
    for i in range(N):
        ans += b[i] - a[i]
    print(ans)

elif step == 2:
    c = []
    for i in range(N):
        c.append(b[i] - a[i])
    d = []
    for i in range(max(c)):
        d.append(i)
    for i in range(len(d)):
        for j in range(len(c)):
            if c[j] - i > 0:
                d[i] += -(-(c[j] - i) // X)
    print(d)
