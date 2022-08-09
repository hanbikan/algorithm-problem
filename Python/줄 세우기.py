import sys

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
degree = [0 for _ in range(N+1)]

for _ in range(M):
    inputL, inputR = map(int, input().split())
    degree[inputR] += 1
    graph[inputL].append(inputR)

todo = []
for i in range(1, N+1):
    if degree[i] == 0:
        todo.append(i)

while todo:
    curHead = todo.pop(0)

    for node in graph[curHead]:
        degree[node] -= 1
        if degree[node] == 0:
            todo.append(node)
    print(curHead, end=" ")
