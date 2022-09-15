from queue import PriorityQueue
import sys
input = sys.stdin.readline

MAX = 501
SAFE, DANGER, DEAD = 0, 1, 2

dx = [1,-1,0,0]
dy = [0,0,1,-1]

mapp = [[SAFE]*MAX for _ in range(MAX)]
N = int(input())
for _ in range(N):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(min(x1, x2), max(x1, x2) + 1):
        for j in range(min(y1, y2), max(y1, y2) + 1):
            mapp[i][j] = DANGER

M = int(input())
for _ in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(min(x1, x2), max(x1, x2) + 1):
        for j in range(min(y1, y2), max(y1, y2) + 1):
            mapp[i][j] = DEAD

# Dijkstra
pq = PriorityQueue()
pq.put([0, 0, 0]) # dist, x, y
dists = [[float('inf')]*MAX for _ in range(MAX)]
while not pq.empty():
    cur_dist, cur_x, cur_y = pq.get()
    for k in range(4):
        nx, ny = cur_x + dx[k], cur_y + dy[k]
        if not (0 <= nx < MAX and 0 <= ny < MAX): continue
        if mapp[nx][ny] == DEAD: continue

        next_dist = cur_dist
        if mapp[nx][ny] == DANGER: next_dist += 1
        
        if dists[nx][ny] > next_dist:
            dists [nx][ny] = next_dist
            pq.put([next_dist, nx, ny])

res = dists[-1][-1]
if res == float('inf'):
    res = -1
print(res)