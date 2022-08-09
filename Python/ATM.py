import sys
read = sys.stdin.readline

N = int(read())
P = list(map(int, read().strip().split()))

curTime = 0
sumTime = 0

P.sort()
for i in range(N):
    sumTime += curTime + P[i]
    curTime += P[i]

print(sumTime)