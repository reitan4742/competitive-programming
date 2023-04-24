S = input()
flag = True
if not S[0] == "A":
    flag = False

count = 0
for i in range(2,len(S)-1):
    if S[i] == "C":
        count += 1

if not count == 1:
    flag = False

count = 0
for s in S:
    if "A" <= s and s <= "Z":
        count += 1

if not count == 2:
    flag = False

if flag:
    print("AC")
else:
    print("WA")