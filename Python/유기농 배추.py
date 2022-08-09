import sys
read = sys.stdin.readline
sys.setrecursionlimit(10000) 

def getMap(M, N, listCabbagesPos):
    RET = [[0]*N for _ in range(M)]
    for cabbagePos in listCabbagesPos:
        RET[cabbagePos[0]][cabbagePos[1]] = 1
    return RET

def dfs(x, y, isVisited, MAP):
    isVisited[x][y] = 1
    if x-1>=0 and not isVisited[x-1][y] and MAP[x-1][y]: dfs(x-1, y, isVisited, MAP)
    if y-1>=0 and not isVisited[x][y-1] and MAP[x][y-1]: dfs(x, y-1, isVisited, MAP)
    if x+1<=M-1 and not isVisited[x+1][y] and MAP[x+1][y]: dfs(x+1, y, isVisited, MAP)
    if y+1<=N-1 and not isVisited[x][y+1] and MAP[x][y+1]: dfs(x, y+1, isVisited, MAP)

def getBugsAmount(M, N, K):
    RET=0
    M, N, K = M, N, K
    listCabbagesPos = []

    for i in range(K):
        listCabbagesPos.append(list(map(int, read().strip().split())))

    MAP = getMap(M, N, listCabbagesPos)
    isVisited = [[0]*N for _ in range(M)]

    for i in range(M):
        for j in range(N):
            if not isVisited[i][j] and MAP[i][j]:
                dfs(i, j, isVisited, MAP)
                RET+=1
                
    return RET

T = int(read())
for i in range(T):
    M, N, K = map(int, read().strip().split())
    print(getBugsAmount(M, N, K))