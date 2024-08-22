import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(node):
    result = 1
    for next_node in graph[node]:
        if is_visited[next_node]:
            continue
        is_visited[next_node] = True
        result += dfs(next_node)
        is_visited[next_node] = False
    dp[node] = result
    return result

N, R, Q = map(int, input().split())
graph = {i:[] for i in range(1, N + 1)}
for _ in range(N - 1):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

dp = [0] * (N + 1)
is_visited = [False] * (N + 1)
is_visited[R] = True
dfs(R)

for _ in range(Q):
    U = int(input())
    print(dp[U])