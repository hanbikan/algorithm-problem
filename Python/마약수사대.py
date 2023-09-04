from collections import defaultdict
import sys
input = sys.stdin.readline

def dfs(node):
    global count
    if not graph.get(node): return
    for next_node in graph[node]:
        if not is_visited[next_node] and not next_node in found:
            is_visited[next_node] = True
            count += 1
            dfs(next_node)

# Input
N, M = map(int, input().split())
graph = {chr(ord('A') + i): [] for i in range(26)}
provide_and_get = {chr(ord('A') + i): [0,0] for i in range(26)}
for _ in range(M):
    a, b = map(str, input().split())
    graph[a].append(b)
    provide_and_get[a][0] += 1
    provide_and_get[b][1] += 1
found = set(list(map(str, input().split()))[1:])

# Find a source of the drugs
sources = []
for key, (provide, get) in provide_and_get.items():
    if provide >= 1 and get == 0:
        sources.append(key)

# Set up for DFS
is_visited = {chr(ord('A') + i): False for i in range(26)}

# DFS
count = 0
for source in sources:
    if source not in found:
        is_visited[source] = True
        dfs(source)

print(count)