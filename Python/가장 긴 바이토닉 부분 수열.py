N = int(input())
A = list(map(int, input().split()))

dpAscend = [0]*N
for i in range(N):
    for j in range(i):
        if A[i]>A[j] and dpAscend[i]<=dpAscend[j]:
            dpAscend[i] = dpAscend[j]+1

dpDescend = [0]*N
for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if A[i]>A[j] and dpDescend[i]<=dpDescend[j]:
            dpDescend[i] = dpDescend[j]+1

RET = 0
for i in range(N):
    RET = max(RET, dpAscend[i]+dpDescend[i]+1)
print(RET)