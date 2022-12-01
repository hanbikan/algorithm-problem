import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def f(node):
    global count
    for next_node in graph[node]:
        if not is_visited[next_node]:
            count += 1
            is_visited[next_node] = True
            f(next_node)

n, m = map(int,input().split())
graph = {i: [] for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int,input().split())
    graph[b].append(a)

X = int(input())

is_visited = [False]*(n+1)
count = 0
is_visited[X] = True
f(X)
print(count)