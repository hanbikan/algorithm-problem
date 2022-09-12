from collections import deque
import sys
input = sys.stdin.readline
CREATE, DESTROY = 1, 2

def f():
    q = deque([1])
    dist = [float('inf')]*(n+1)
    dist[1] = 0
    while len(q) > 0:
        cur_node = q.popleft()
        for next_node in range(1, n+1):
            if graph[cur_node][next_node] == False: continue
            if dist[next_node] > dist[cur_node] + 1:
                dist[next_node] = dist[cur_node] + 1
                q.append(next_node)
                
    for i in range(1, n+1):
        print(dist[i] if dist[i] != float('inf') else -1, end = " ")
    print()

n, m = map(int, input().split())
graph = [[False]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True
    
q = int(input())
for _ in range(q):
    a, i, j = map(int, input().split())
    if a == CREATE:
        graph[i][j] = True
        graph[j][i] = True
        f()
    else:
        graph[i][j] = False
        graph[j][i] = False
        f()