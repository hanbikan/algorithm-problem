
DESTINATION, WEIGHT = 0, 1
V, E = map(int, input().split())
K = int(input())
graph = {i:{} for i in range(V+1)}

for i in range(E):
    u, v, w = map(int, input().split())
    if graph[u].get(v):
        graph[u][v] = min(graph[u][v], w)
    else:
        graph[u][v] = w

print(graph)
RET = [None]*(V+1)

todo = [[K, 0]] #[[2, 2], [3, 3]] -> [[3, 6], [4, 7], ..., ]
isVisited = [False]*(V+1)
while todo:
    nextTodo = []
    for cur in todo:
        curDestination, curAccumulatedWeight = cur[DESTINATION], cur[WEIGHT]

        if RET[curDestination]!=None: RET[curDestination] = min(RET[curDestination], curAccumulatedWeight)
        else: RET[curDestination] = curAccumulatedWeight

        for key in graph[curDestination]:
            if not isVisited[key]:
                nextTodo.append([key, curAccumulatedWeight+graph[curDestination][key]])
                isVisited[key] = True
    todo = nextTodo

for i in range(1, V+1):
    if RET[i]!=None: print(RET[i])
    else: print('INF')