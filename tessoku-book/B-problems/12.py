N = int(input())
L = 0
R = 46.0

while True:
    M = (L + R)/2.0
    tmp = M**3 + M
    if tmp < N - 0.001:
        L = M
    elif tmp > N + 0.001:
        R = M
    else:
        print(M)
        break