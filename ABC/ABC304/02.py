N = int(input())
if N <= 10**3 -1:
  pass
elif 10**3 <= N <= 10**4 -1:
  N /= 10
  N = int(N) * 10
elif 10**4 <= N <= 10**5 -1:
  N /= 10**2
  N = int(N) * 10**2
elif 10**5 <= N <= 10**6 -1:
  N /= 10**3
  N = int(N) * 10**3
elif 10**6 <= N <= 10**7 -1:
  N /= 10**4
  N = int(N) * 10**4
elif 10**7 <= N <= 10**8 -1:
  N /= 10**5
  N = int(N) * 10**5
else:
  N /= 10**6
  N = int(N) * 10**6

print(N)