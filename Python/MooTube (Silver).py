import sys, collections
input = sys.stdin.readline

def bfs(start_node):
    q = collections.deque([(start_node, float('inf'))])
    is_visited = [False] * (N + 1)
    is_visited[start_node] = True

    while q:
        node, u = q.popleft()
        for next_u, next_node in graph[node]:
            if is_visited[next_node]:
                continue

            is_visited[next_node] = True
            next_min_u = min(u, next_u)
            usado[start_node][next_node] = next_min_u
            q.append((next_node, next_min_u))

N, Q = map(int, input().split())

graph = {i: [] for i in range(1, N + 1)}
usado = [[float('inf')] * (N + 1) for i in range(N + 1)]
for _ in range(N - 1):
    p, q, r = map(int, input().split())
    graph[p].append((r, q))
    graph[q].append((r, p))
    usado[p][q] = r
    usado[q][p] = r

for i in range(1, N + 1):
    bfs(i)

for _ in range(Q):
    k, v = map(int, input().split())
    count = 0
    for i in range(1, N + 1):
        if i == v:
            continue
        if usado[i][v] >= k:
            count += 1
    print(count)
