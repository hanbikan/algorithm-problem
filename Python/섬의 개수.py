import sys
sys.setrecursionlimit(10000)

SEA, LAND, CONSIDERED = 0, 1, 2
def getAmountOfLand():
    global Map
    #처음에 모든 Land 영역 TODO에 넣음
    TODO = []
    for i in range(len(Map)):
        for j in range(len(Map[i])):
            if Map[i][j]==LAND: TODO.append([i, j])

    #TODO 따라서 dfs ... 단, 1번 방문한 LAND는 CONSIDERED로 전환
    RET = 0
    for curPos in TODO:
        x, y = curPos[0], curPos[1]
        if(Map[x][y]==CONSIDERED): continue #이미 방문했을 경우 스킵

        RET += 1
        dfs(x, y)

    return RET

def dfs(x, y):
    global Map, w, h
    Map[x][y] = CONSIDERED
    if x-1>=0 and Map[x-1][y]==LAND: dfs(x-1, y)
    if y-1>=0 and Map[x][y-1]==LAND: dfs(x, y-1)
    if x+1<h and Map[x+1][y]==LAND: dfs(x+1, y)
    if y+1<w and Map[x][y+1]==LAND: dfs(x, y+1)
    if (x-1>=0 and y-1>=0) and Map[x-1][y-1]==LAND: dfs(x-1, y-1)
    if (x-1>=0 and y+1<w) and Map[x-1][y+1]==LAND: dfs(x-1, y+1)
    if (x+1<h and y-1>=0) and Map[x+1][y-1]==LAND: dfs(x+1, y-1)
    if (x+1<h and y+1<w) and Map[x+1][y+1]==LAND: dfs(x+1, y+1)

w, h = map(int, input().split())
while not (w==0 and h==0):
    Map = []
    for i in range(h): Map.append(list(map(int, input().split())))
    print(getAmountOfLand())

    w, h = map(int, input().split())