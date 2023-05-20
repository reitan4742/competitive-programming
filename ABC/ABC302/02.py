H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(input())

ans = []
for i in range(W):
    for j in range(H):
        if S[j][i] == "s":
            if i + 4 < W:
                if S[j][i+1] == "n" and S[j][i+2] == "u" and S[j][i+3] == "k" and S[j][i+4] == "e":
                    for k in range(5):
                        ans.append([j,i+k])
                    break
                if j+4 < H:
                    if S[j+1][i+1] == "n" and S[j+2][i+2] == "u" and S[j+3][i+3] == "k" and S[j+4][i+4] == "e":
                        for k in range(5):
                            ans.append([j+k,i+k])
                        break
                if j-4 >= 0:
                    if S[j-1][i+1] == "n" and S[j-2][i+2] == "u" and S[j-3][i+3] == "k" and S[j-4][i+4] == "e":
                        for k in range(5):
                            ans.append([j-k,i+k])
                        break

            if i - 4 >= 0:
                if S[j][i-1] == "n" and S[j][i-2] == "u" and S[j][i-3] == "k" and S[j][i-4] == "e":
                    for k in range(5):
                        ans.append([j,i-k])
                    break
                if j+4 < H:
                    if S[j+1][i-1] == "n" and S[j+2][i-2] == "u" and S[j+3][i-3] == "k" and S[j+4][i-4] == "e":
                        for k in range(5):
                            ans.append([j+k,i-k])
                        break
                if j-4 >= 0:
                    if S[j-1][i-1] == "n" and S[j-2][i-2] == "u" and S[j-3][i-3] == "k" and S[j-4][i-4] == "e":
                        for k in range(5):
                            ans.append([j-k,i-k])
                        break
            if j +4 < H:
                if S[j+1][i] == "n" and S[j+2][i] == "u" and S[j+3][i] == "k" and S[j+4][i] == "e":
                    for k in range(5):
                        ans.append([j+k,i])
                    break
            if j -4 >= 0:
                if S[j-1][i] == "n" and S[j-2][i] == "u" and S[j-3][i] == "k" and S[j-4][i] == "e":
                    for k in range(5):
                        ans.append([j-k,i])
                    break
    else:
        continue
    break

for i in range(len(ans)):
    print(str(ans[i][0]+1)+" "+str(ans[i][1]+1))
