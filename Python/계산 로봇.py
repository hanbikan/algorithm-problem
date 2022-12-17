import sys
input = sys.stdin.readline

# Input
N, M = map(int,input().split())
mapp = []
for _ in range(N):
    line = []
    for c in input().rstrip():
        line.append(int(c))
    mapp.append(line)

# Calculate
saved = [[0]*M for _ in range(N)]
for j in range(1, M):
    for i in range(N):
        saved[i][j] = saved[i][j-1] + mapp[i][j-1]
        if i-1 >= 0 and j-1 >= 0:
            saved[i][j] = max(saved[i][j], saved[i-1][j-1] + mapp[i-1][j-1])
        if i+1 <= N-1 and j-1 >= 0:
            saved[i][j] = max(saved[i][j], saved[i+1][j-1] + mapp[i+1][j-1])

res = 0
for i in range(N):
    res = max(res, saved[i][-1])
print(res)