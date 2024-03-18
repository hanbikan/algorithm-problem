import sys
input = sys.stdin.readline

def get_reacheable_count(g, node):
    result = 1
    is_visited[node] = True
    for next_node in g[node]:
        if is_visited[next_node]: continue
        result += get_reacheable_count(g, next_node)
    return result

N, M = map(int,input().split())

graph = {i: [] for i in range(1, N + 1)}
graph_reversed = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph_reversed[b].append(a)

result = 0
for i in range(1, N + 1):
    is_visited = [False] * (N + 1)
    count1 = get_reacheable_count(graph, i) - 1
    count2 = get_reacheable_count(graph_reversed, i) - 1

    if count1 + count2 == N - 1:
        result += 1

print(result)