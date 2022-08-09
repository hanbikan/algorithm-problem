import sys
input = sys.stdin.readline


def bfs(x, y):
    global maxSpentTime
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    spentTimeMap = [[-1]*M for _ in range(N)]
    spentTimeMap[x][y] = 0

    todo = [(x, y)]
    while todo:
        x, y = todo.pop(0)
        for i in range(4):
            curX = x+dx[i]
            curY = y+dy[i]
            if (0 <= curX <= N-1 and 0 <= curY <= M-1):
                if Map[curX][curY] == 'L' and spentTimeMap[curX][curY] == -1:
                    spentTimeMap[curX][curY] = spentTimeMap[x][y]+1
                    maxSpentTime = max(maxSpentTime, spentTimeMap[curX][curY])
                    todo.append((curX, curY))


N, M = map(int, input().split())
Map = []
for _ in range(N):
    curLine = input().rstrip()

    curMapLine = []
    for c in curLine:
        curMapLine.append(c)
    Map.append(curMapLine)

maxSpentTime = -1
for i in range(N):
    for j in range(M):
        if Map[i][j] == 'L':
            bfs(i, j)

print(maxSpentTime)
