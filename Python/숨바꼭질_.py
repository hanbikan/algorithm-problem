import sys
input = sys.stdin.readline

N, M = map(int,input().split())
graph = {i: [] for i in range(1,N+1)}
for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

q = [[1, 0]]
dist = [float('inf')]*(N+1)
dist[1] = 0

while len(q) > 0:
    cur_node, cur_dist = q.pop(0)

    for next_node in graph[cur_node]:
        next_dist = cur_dist + 1
        if dist[next_node] > next_dist:
            dist[next_node] = next_dist
            q.append([next_node, next_dist])

max_dist = 0
max_node = 1
max_count = 1
for i in range(1, N+1):
    if max_dist < dist[i]:
        max_dist = dist[i]
        max_node = i
        max_count = 1
    elif max_dist == dist[i]:
        max_count += 1

print(max_node, max_dist, max_count)