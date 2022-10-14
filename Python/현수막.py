import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

dx = [-1,-1,-1,0,1,1,1,0]
dy = [-1,0,1,1,1,0,-1,-1]

def f(x, y):
    for k in range(8):
        nx, ny = x + dx[k], y + dy[k]
        if not (0 <= nx <= N-1 and 0 <= ny <= M-1): continue
        if is_visited[nx][ny]: continue
        if mapp[nx][ny] == 0: continue

        is_visited[nx][ny] = True
        f(nx, ny)

N, M = map(int,input().split())
mapp = [list(map(int,input().split())) for _ in range(N)]

is_visited = [[False]*M for _ in range(N)]
res = 0
for i in range(N):
    for j in range(M):
        if is_visited[i][j]: continue
        if mapp[i][j] == 0: continue

        is_visited[i][j] = True
        f(i,j)
        res += 1

print(res)