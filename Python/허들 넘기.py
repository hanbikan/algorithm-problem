import sys
input = sys.stdin.readline

NODE, HEIGHT = 0, 1

N,M,T = map(int,input().split())
graph = {i: [] for i in range(1,N+1)}
dist = [[float('inf')]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    dist[i][i] = 0
for i in range(M):
    u,v,h = map(int,input().split())
    graph[u].append([v,h])
    dist[u][v] = h
is_visited = [False]*(N+1)

# FW
for k in range(1, N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            dist[i][j] = min(dist[i][j], max(dist[i][k], dist[k][j]))

for i in range(T):
    s,e = map(int,input().split())
    if dist[s][e] == float('inf'):
        print(-1)
    else:
        print(dist[s][e])