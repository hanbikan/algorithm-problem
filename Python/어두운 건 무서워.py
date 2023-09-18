import sys
input = sys.stdin.readline

R, C, Q = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(R)]

# Prefix sum
prefix_sum_map = [[0]*C]
for i in range(R):
    cur = 0
    line = [0]
    for j in range(C):
        line.append(cur + mapp[i][j])
        cur = line[-1]
    prefix_sum_map.append(line)

for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    summ = 0
    for i in range(r1, r2 + 1):
        summ += prefix_sum_map[i][c2] - prefix_sum_map[i][c1 - 1]
    area = (r2 - r1 + 1) * (c2 - c1 + 1)

    print(summ // area)