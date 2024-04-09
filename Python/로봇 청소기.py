import sys
input = sys.stdin.readline

NOT_CLEAN, WALL, CLEAN = 0, 1, 2
d_pos = [[-1,0],[0,1],[1,0],[0,-1]]

def in_range(x, y):
    return 0 <= x <= N - 1 and 0 <= y <= M - 1

N, M = map(int,input().split())
r, c, d = map(int,input().split())

mapp = [list(map(int,input().split())) for _ in range(N)]

count = 0
while True:
    # 1
    if mapp[r][c] == NOT_CLEAN:
        mapp[r][c] = CLEAN
        count += 1
    
    # Check adjacents
    is_there_not_clean_adj = False
    for dx, dy in d_pos:
        nx, ny = r + dx, c + dy
        if not in_range(nx, ny):
            continue
        if mapp[nx][ny] == NOT_CLEAN:
            is_there_not_clean_adj = True
            break
    
    if not is_there_not_clean_adj: # 2
        dx, dy = d_pos[(d + 2) % 4]
        nx, ny = r + dx, c + dy
        if in_range(nx, ny) and mapp[nx][ny] != WALL:
            r, c = nx, ny
        else:
            break
    else: # 3
        d = (d + 3) % 4
        dx, dy = d_pos[d]
        nx, ny = r + dx, c + dy
        if in_range(nx, ny) and mapp[nx][ny] == NOT_CLEAN:
            r, c = nx, ny

print(count)