import sys
input = sys.stdin.readline

def reachable_to_x(node):
    result = 1
    is_visited[node] = True
    for next_node in rev_graph[node]:
        if is_visited[next_node]:
            continue
        result += reachable_to_x(next_node)
    return result

def reachable_by_x(node):
    result = 1
    is_visited[node] = True
    for next_node in graph[node]:
        if is_visited[next_node]:
            continue
        result += reachable_by_x(next_node)
    return result

N, M, X = map(int,input().split())
graph = {i: [] for i in range(1, N + 1)}
rev_graph = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    A, B = map(int,input().split())
    graph[A].append(B)
    rev_graph[B].append(A)

is_visited = [False] * (N + 1)
U = 1 + (reachable_to_x(X) - 1)
V = N - (reachable_by_x(X) - 1)

print(U, V)