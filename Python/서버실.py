import sys, math
input = sys.stdin.readline

N = int(input())
mapp = [list(map(int,input().split())) for _ in range(N)]

total_count = 0
max_h = 0
for i in range(N):
    for j in range(N):
        if mapp[i][j] == 0: continue
        total_count += mapp[i][j]
        max_h = max(max_h, mapp[i][j])

l, r = 0, max_h
result = 0
while l <= r:
    m = (l + r) // 2
    cur = 0
    for i in range(N):
        for j in range(N):
            cur += min(m, mapp[i][j])

    if cur >= math.ceil(total_count / 2):
        result = m
        r = m - 1
    else:
        l = m + 1
print(result)

'''
2
10 10
10 10

1
7
'''