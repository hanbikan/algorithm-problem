import sys, copy

input = sys.stdin.readline

d_pos = [[0,1],[0,-1],[1,0],[-1,0]]

def in_range(x, y):
    return 0 <= x < H and 0 <= y < W

def get_adj_count(x, y, value):
    result = 1
    visited[x][y] = True
    for dx, dy in d_pos:
        nx, ny = x + dx, y + dy
        if not in_range(nx, ny): continue
        if visited[nx][ny]: continue
        if mapp[nx][ny] != value: continue
        result += get_adj_count(nx, ny, value)
    return result

def pop(x, y, value):
    mapp[x][y] = '.'
    for dx, dy in d_pos:
        nx, ny = x + dx, y + dy
        if not in_range(nx, ny): continue
        if mapp[nx][ny] != value: continue
        pop(nx, ny, value)


mapp = [list(input().rstrip()) for _ in range(12)]
W, H = 6, 12

combo = 0
while True:
    # find 4 adj
    visited = [[False]*W for _ in range(H)]
    to_pop = []
    for i in range(H):
        for j in range(W):
            if mapp[i][j] == '.': continue
            adj_count = get_adj_count(i, j, mapp[i][j])
            if adj_count >= 4:
                to_pop.append((i, j))

    if len(to_pop) == 0:
        break
    combo += 1
    # pop
    for x, y in to_pop:
        pop(x, y, mapp[x][y])

    #for i in range(H): print(mapp[i])
    #print()

    # apply gravity
    for j in range(W):
        blocks_only = []
        for i in range(H - 1, -1, -1):
            if mapp[i][j] != '.':
                blocks_only.append(mapp[i][j])
        offset = 0
        for i in range(H - 1, -1, -1):
            if offset < len(blocks_only):
                mapp[i][j] = blocks_only[offset]
            else:
                mapp[i][j] = '.'
            offset += 1

    #for i in range(H): print(mapp[i])
    #print()

print(combo)

'''
......
......
......
......
......
......
......
......
......
PPGGG.
PPYYG.
RRYYG.

......
P.....
RRRRRR
RRRRRR
P.....
P.....
P.....
RRRRRR
P.....
P.....
RRRRRR
RRRRRR

......
......
......
P.....
RRRRRR
RRRRRR
P.....
P.....
P.....
RRRRRR
P.....
P.....
'''