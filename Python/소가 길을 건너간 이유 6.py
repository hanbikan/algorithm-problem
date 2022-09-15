from collections import deque
import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dijkstra(cow):
    q = deque([cow])
    is_visited = [[False]*(N+1) for _ in range(N+1)]

    while len(q) > 0:
        cur_x, cur_y = q.popleft()

        for k in range(4):
            nx, ny = cur_x + dx[k], cur_y + dy[k]
            if not (1 <= nx <= N and 1 <= ny <= N): continue
            if is_visited[nx][ny]: continue
            if nx*N+ny in bridges[cur_x*N+cur_y]: continue

            q.append([nx,ny])
            is_visited[nx][ny] = True
    
    return is_visited


N, K, R = map(int,input().split())
bridges = {i: set() for i in range(N*N+N+1)}
for _ in range(R):
    r1, c1, r2, c2 = map(int,input().split())
    bridges[r1*N+c1].add(r2*N+c2)
    bridges[r2*N+c2].add(r1*N+c1)

cows = []
for _ in range(K):
    r, c = map(int,input().split())
    cows.append([r,c])

res = 0
for i in range(K):
    is_visited = dijkstra(cows[i])
    for j in range(i+1, K):
        r, c = cows[j]
        if not is_visited[r][c]:
            res += 1

print(res)