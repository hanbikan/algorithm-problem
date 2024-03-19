import sys
input = sys.stdin.readline

def is_reachable(node, target):
    is_visited[node] = True
    if target == node:
        return True
    for next_node in graph[node]:
        if is_visited[next_node]: continue

        if is_reachable(next_node, target):
            return True
    
    return False

n = int(input())
graph = {chr(ord('a') + i): [] for i in range(ord('z') - ord('a') + 1)}

for _ in range(n):
    cur = str(input().rstrip())
    a, b = cur[0], cur[-1]
    graph[a].append(b)

m = int(input())
for _ in range(m):
    cur = str(input().rstrip())
    a, b = cur[0], cur[-1]
    is_visited = {chr(ord('a') + i): False for i in range(ord('z') - ord('a') + 1)}
    if is_reachable(a, b):
        print('T')
    else:
        print('F')