import sys
input = sys.stdin.readline

dx = [-1,-1,-1,0,1,1,1,0]
dy = [-1,0,1,1,1,0,-1,-1]

H,W = map(int,input().split())
mapp = [list(str(input().rstrip())) for _ in range(H)]

dot_counts = [[0]*W for _ in range(H)]
to_remove = []
for x in range(H):
    for y in range(W):
        if mapp[x][y] == '.':
            continue
        dot_count = 0
        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if mapp[nx][ny] == '.':
                dot_count += 1
        dot_counts[x][y] = dot_count
        if dot_count >= int(mapp[x][y]):
            to_remove.append((x,y))

if len(to_remove) == 0:
    print(0)
else:
    turn = 1
    while True:
        #print(to_remove)
        for x, y in to_remove:
            mapp[x][y] = '.'
            dot_counts[x][y] = 0

        next_to_remove = set()
        for x, y in to_remove:
            for k in range(8):
                nx, ny = x + dx[k], y + dy[k]
                if mapp[nx][ny] == '.':
                    continue
                dot_counts[nx][ny] = dot_counts[nx][ny] + 1
                if dot_counts[nx][ny] >= int(mapp[nx][ny]):
                    next_to_remove.add((nx, ny))

        to_remove = list(next_to_remove)
        #for m in mapp: print(m)
        #for d in dot_counts: print(d)

        # check same?
        if len(to_remove) == 0:
            break

        turn += 1

    print(turn)