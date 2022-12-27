import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def f():
    q = [[x1,y1]]
    pos_to_remove = []
    is_visited = [[False]*M for _ in range(N)]
    is_visited[x1][y1] = True

    while len(q) > 0:
        x, y = q.pop(0)
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if not (0 <= nx <= N-1 and 0 <= ny <= M-1): continue
            if is_visited[nx][ny]: continue

            if mapp[nx][ny] == "0":
                q.append([nx,ny])
                is_visited[nx][ny] = True
            elif mapp[nx][ny] == "1":
                pos_to_remove.append([nx,ny])
            elif mapp[nx][ny] == "#":
                return True
                
    for x, y in pos_to_remove:
        mapp[x][y] = "0"

    return False

# Input
N, M = map(int,input().split())
x1, y1, x2, y2 = map(int,input().split())
x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1

mapp = []
for _ in range(N):
    line = []
    for c in input().rstrip():
        line.append(c)
    mapp.append(line)

# Solution
jump = 1
while True:
    if f():
        print(jump)
        break
    jump += 1