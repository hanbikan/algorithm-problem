import sys
input = sys.stdin.readline

def dfs(node, visited):
    result = float('inf')
    visited.add(node)

    for next_node in range(N):
        if next_node == node or next_node in visited:
            continue

        result = min(result, dfs(next_node, visited) + costs[node][next_node])
    
    visited.remove(node)
    return result if result != float('inf') else 0

N, T = map(int,input().split())
costs = [list(map(int,input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            costs[i][j] = min(costs[i][j], costs[i][k] + costs[k][j])

print(dfs(T, set()))