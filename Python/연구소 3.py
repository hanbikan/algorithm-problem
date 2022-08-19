from copy import deepcopy
from itertools import combinations
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
EMPTY, WALL, VIRUS, INFECTED_SPACE, INFECTED_VIRUS = 0, 1, 2, 3, 4
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def f(current_viruses, infected_count, time):
    global mapp

    if len(current_viruses) == 0: return float('inf')
    if (infected_count >= empty_count): return time

    next_viruses = []
    for x, y in current_viruses:
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if not (0 <= nx <= N-1 and 0 <= ny <= N-1): continue

            item = mapp[nx][ny]
            if item == EMPTY or item == VIRUS:
                next_viruses.append([nx,ny])
                if (item == EMPTY): infected_count += 1
                mapp[nx][ny] = INFECTED_SPACE if (item == EMPTY) else INFECTED_VIRUS

    res = f(next_viruses, infected_count, time + 1)

    for x, y in next_viruses:
        mapp[x][y] = EMPTY if mapp[x][y] == INFECTED_SPACE else VIRUS

    return res

N, M = map(int,input().split())
mapp = [list(map(int,input().split())) for _ in range(N)]
viruses = []
empty_count = 0

for i in range(N):
    for j in range(N):
        if mapp[i][j] == VIRUS:
            viruses.append([i, j])
        if mapp[i][j] == EMPTY:
            empty_count += 1

res = float('inf')
for positions in combinations(viruses, M):
    for x, y in positions:
        mapp[x][y] = INFECTED_VIRUS

    res = min(res, f(positions, 0, 0))

    for x, y in positions:
        mapp[x][y] = VIRUS

if res == float('inf'):
    print(-1)
else:
    print(res)