from copy import deepcopy
import sys
input = sys.stdin.readline

EMPTY = 0
WATCHED = 7
WALL = 6

dx = [0,-1,0,1]
dy = [1,0,-1,0]

start_directions = [[], [0], [0,2], [0,1], [0,1,2], [0,1,2,3]]

def print_mapp():
    for i in range(N):
        print(*mapp[i])
    print()

def watch_for_cctv(x, y, cctv, dir):
    for start_direction in start_directions[cctv]:
        watch(x, y, (dir + start_direction) % 4)

def watch(x, y, dir):
    global mapp
    while (0 <= x <= N - 1 and 0 <= y <= M - 1):
        if mapp[x][y] == WALL:
            break
        elif mapp[x][y] == EMPTY:
            mapp[x][y] = WATCHED
        x += dx[dir]
        y += dy[dir]

def dfs_with_cctvs(cctvs, cctvs_index):
    global mapp
    if cctvs_index >= len(cctvs):
        # Calculate the size of the blind spots
        res = 0
        for i in range(N):
            for j in range(M):
                if mapp[i][j] == 0:
                    res += 1
        return res
    
    res = float('inf')
    x, y = cctvs[cctvs_index]
    cctv = mapp[x][y]

    original = deepcopy(mapp)
    if cctv == 1 or cctv == 3 or cctv == 4:
        for k in range(4):
            watch_for_cctv(x, y, cctv, k)
            res = min(res, dfs_with_cctvs(cctvs, cctvs_index + 1))
            mapp = deepcopy(original)
    elif cctv == 2:
        for k in range(2):
            watch_for_cctv(x, y, cctv, k)
            res = min(res, dfs_with_cctvs(cctvs, cctvs_index + 1))
            mapp = deepcopy(original)
    else:
        watch_for_cctv(x, y, cctv, 0)
        res = min(res, dfs_with_cctvs(cctvs, cctvs_index + 1))
        mapp = deepcopy(original)

    return res


N, M = map(int,input().split())
mapp = [list(map(int,input().split())) for _ in range(N)]

# Set cctvs
cctvs = []
for i in range(N):
    for j in range(M):
        if 1 <= mapp[i][j] and mapp[i][j] <= 5:
            cctvs.append([i,j])

# DFS with cctvs
print(dfs_with_cctvs(cctvs, 0))