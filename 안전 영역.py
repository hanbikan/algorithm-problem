import sys
sys.setrecursionlimit(20000)

input = sys.stdin.readline

N = int(input())
Map = []
for _ in range(N):
    Map.append(list(map(int, input().split())))

stateMap = None


def getSafeZone(h):
    global stateMap
    stateMap = [[0]*N for _ in range(N)]
    cntSafeZone = 0
    for i in range(N):
        for j in range(N):
            if Map[i][j] > h and stateMap[i][j] == 0:
                cntSafeZone += 1
                dfs(i, j, h)
    return cntSafeZone


def dfs(x, y, h):
    global stateMap
    stateMap[x][y] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        curX, curY = x+dx[i], y+dy[i]
        if(0 <= curX <= N-1 and 0 <= curY <= N-1):
            if stateMap[curX][curY] == 0:
                if Map[curX][curY] > h:
                    dfs(curX, curY, h)


maxSafeZone = 0
for i in range(0, 101):
    cur = getSafeZone(i)
    if cur == 0:
        break
    maxSafeZone = max(maxSafeZone, cur)
print(maxSafeZone)
