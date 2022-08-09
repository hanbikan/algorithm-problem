N = int(input())
adjacencyMatrix = []
for i in range(N):
    adjacencyMatrix.append(list(map(int, input().split())))

graph = {i:[] for i in range(N)}
for i in range(N):
    for j in range(N):
        if adjacencyMatrix[i][j]==1:
            graph[i].append(j)

RET = [[0]*N for _ in range(N)]
for i in range(N):
    isVisited = [False]*N
    TODO = graph[i]
    while TODO:
        nextTODO = []
        for td in TODO:
            if not isVisited[td]:
                nextTODO+=graph[td]
                isVisited[td] = True
                RET[i][td] = 1
        TODO=nextTODO
for i in range(N):
    for j in range(N): print(RET[i][j], end=" ")
    print()