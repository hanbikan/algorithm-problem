import sys
sys.setrecursionlimit(10000)
def dfs(x, y):
    global curArea, Map
    curArea+=1
    Map[x][y] = 1
    if x-1>=0 and Map[x-1][y]==0: dfs(x-1, y)
    if y-1>=0 and Map[x][y-1]==0: dfs(x, y-1)
    if x+1<=M-1 and Map[x+1][y]==0: dfs(x+1, y)
    if y+1<=N-1 and Map[x][y+1]==0: dfs(x, y+1)

M, N, K = map(int, input().split())
Map = [[0]*N for _ in range(M)]
for i in range(K):
    y1,x2,y2,x1 = map(int, input().split())
    x1, x2 = M-x1, M-x2
    for i in range(x1, x2):
        for j in range(y1, y2):
            Map[i][j] = 1

cntArea = 0
areas = []
for i in range(M):
    for j in range(N):
        if Map[i][j] == 0:
            cntArea += 1
            curArea = 0
            dfs(i,j)
            areas.append(curArea)
areas.sort()
print(cntArea)
for i in range(cntArea): print(areas[i], end=" ")