import sys
input = sys.stdin.readline

W, H = 9, 5

d_pos = [[1,0],[0,1],[-1,0],[0,-1]]

def dfs(move_count):
    global max_move_count

    max_move_count = max(max_move_count, move_count)
        
    for x in range(H):
        for y in range(W):
            if mapp[x][y] == 'o':
                for dx, dy in d_pos:
                    nx, ny = x + dx, y + dy
                    nnx, nny = x + dx * 2, y + dy * 2
                    if not (0 <= nnx < H and 0 <= nny < W): continue
                    if mapp[nx][ny] == 'o' and mapp[nnx][nny] == '.':
                        mapp[x][y] = '.'
                        mapp[nx][ny] = '.'
                        mapp[nnx][nny] = 'o'
                        dfs(move_count + 1)
                        mapp[x][y] = 'o'
                        mapp[nx][ny] = 'o'
                        mapp[nnx][nny] = '.'

T = int(input())
for time in range(T):
    mapp = [list(str(input().rstrip())) for _ in range(H)]

    pin_count = 0
    for i in range(H):
        for c in mapp[i]:
            if c == 'o':
                pin_count += 1

    max_move_count = 0
    dfs(0)
    print(pin_count - max_move_count, max_move_count)

    if time != T - 1:
        input()

'''
1
.........
.oo...oo.
.oo...oo.
.........
.........
'''