import sys, heapq

BLACK, WHITE = '0', '1'

input = sys.stdin.readline
#sys.stdin = open('./meta/input.txt', 'r')
d_pos = [[1,0],[0,1],[-1,0],[0,-1]]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

n = int(input())
mapp = [list(input().rstrip()) for _ in range(n)]

q = [[0, (0, 0)]]
dists = [[float('inf')]*n for _ in range(n)]
dists[0][0] = 0
while q:
    cur_dist, (cur_x, cur_y) = heapq.heappop(q)
    for dx, dy in d_pos:
        nx, ny = cur_x + dx, cur_y + dy
        if not in_range(nx, ny): continue

        next_dist = cur_dist if mapp[nx][ny] == WHITE else cur_dist + 1
        if next_dist < dists[nx][ny]:
            heapq.heappush(q, [next_dist, (nx, ny)])
            dists[nx][ny] = next_dist

print(dists[-1][-1])