import copy, sys
read=sys.stdin.readline
N,M=map(int, read().strip().split())
Map=[]
for i in range(N):
    curLine = list(map(int, read().strip().split()))
    Map.append(curLine)
safeArea=0
amountWalls=0

def setWalls(x,y):
    global amountWalls
    if(amountWalls==3):
        global safeArea
        safeArea = max(safeArea, getSafeArea())
        return

    for i in range(N):
        for j in range(M):
            if Map[i][j]==0 and (N*i+j>N*x+y or (x==0 and y==0)):
                Map[i][j]=1
                amountWalls+=1
                setWalls(i,j)
                amountWalls-=1
                Map[i][j]=0

def getSafeArea():
    global visited
    visited = [[0]*M for _ in range(N)]
    RET=0
    curMap = copy.deepcopy(Map)
    for i in range(N):
        for j in range(M):
            if curMap[i][j]==2 and visited[i][j]==0:
                curMap = virusStart(curMap, i, j)
    for i in range(N):
        for j in range(M):
            if curMap[i][j]==0: RET+=1
    return RET

def virusStart(curMap, x, y):
    curMap[x][y] = 2
    global visited
    visited[x][y]=1
    if(x-1>=0 and curMap[x-1][y]==0):
        curMap = virusStart(curMap, x-1, y)
    if(y-1>=0 and curMap[x][y-1]==0):
        curMap = virusStart(curMap, x, y-1)
    if(x+1<N and curMap[x+1][y]==0):
        curMap = virusStart(curMap, x+1, y)
    if(y+1<M and curMap[x][y+1]==0):
        curMap = virusStart(curMap, x, y+1)
    return curMap

setWalls(0,0)
print(safeArea)