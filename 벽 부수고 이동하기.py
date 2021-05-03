import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    global stepMap

    todo = [(0, 0, 0)]

    while todo:
        curPos = todo.pop(0)
        if curPos[1] == N-1 and curPos[2] == M-1:
            return stepMap[curPos[0]][curPos[1]][curPos[2]]

        for i in range(4):
            curX, curY = curPos[1] + dx[i], curPos[2] + dy[i]

            if 0 <= curX <= N-1 and 0 <= curY <= M-1:
                if map[curX][curY] == 0 and stepMap[curPos[0]][curX][curY] == 0:
                    stepMap[curPos[0]][curX][curY] = stepMap[curPos[0]
                                                             ][curPos[1]][curPos[2]]+1
                    todo.append((curPos[0], curX, curY))
                elif map[curX][curY] == 1 and stepMap[1][curX][curY] == 0 and curPos[0] == 0:
                    stepMap[1][curX][curY] = stepMap[curPos[0]
                                                     ][curPos[1]][curPos[2]]+1
                    todo.append((1, curX, curY))
    return -1


N, M = map(int, input().split())
map = []

for i in range(N):
    curLine = input().rstrip()
    curList = []
    for j in range(M):
        n = int(curLine[j])
        curList.append(n)
    map.append(curList)


stepMap = [[[0]*M for _ in range(N)] for _ in range(2)]
stepMap[0][0][0] = 1

print(bfs())
