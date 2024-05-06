import sys, heapq
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

# dijkstra
q = [[0, X]]
dp = [float('inf')] * (N + 1)
dp[X] = 0
while q:
    cur_dist, cur_node = heapq.heappop(q)
    for next_node in graph[cur_node]:
        next_dist = cur_dist + 1
        if next_dist < dp[next_node]:
            dp[next_node] = next_dist
            heapq.heappush(q, [next_dist, next_node])

# print result
result = []
for i in range(1, N + 1):
    if dp[i] == K:
        result.append(i)

if result:
    for i in result:
        print(i)
else:
    print(-1)