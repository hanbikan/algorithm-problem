import sys
read = sys.stdin.readline
N,M,V=map(int, read().strip().split())
edges = [[] for _ in range(N+1)]

for i in range(M):
    curInput = list(map(int, read().strip().split()))
    edges[curInput[0]].append(curInput[1])
    edges[curInput[1]].append(curInput[0])

for edge in edges: edge.sort(reverse = True)

def dfs():
    RET = []
    stack=[V]
    visited = [False for _ in range(N+1)]
    while stack:
        cur=stack.pop()
        if not visited[cur]:
            visited[cur] = True
            RET.append(cur)
            stack+=edges[cur]
    return RET

def bfs():
    RET = []
    queue=[V]
    visited = [False for _ in range(N+1)]
    visited[V] = True
    while queue:
        cur = queue.pop()
        RET.append(cur)
        for i in reversed(edges[cur]):
            if not visited[i]:
                visited[i] = True
                queue = [i] + queue
    return RET

print(dfs())
print(bfs())