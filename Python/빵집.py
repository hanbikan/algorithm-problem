import sys
input = sys.stdin.readline

R, C = map(int, input().split())
Map = []
for _ in range(R):
    Map.append(list(input())[:-1])
# print(Map)


def getPossiblePos(x, y):
    dx = [-1, 0, 1]
    dy = [1, 1, 1]
    for i in range(3):
        curX = x+dx[i]
        curY = y+dy[i]
        if 0 <= curX <= R-1 and 0 <= curY <= C-1:
            if Map[curX][curY] == '.':
                return (curX, curY)
    return (-1, -1)


def putPipeLine(x):
    listPos = []
    curX, curY = x, 0
    print()
    for i in range(C-1):
        print(curX, curY)
        listPos.append((curX, curY))
        curX, curY = getPossiblePos(curX, curY)
        if curX == -1 and curY == -1:
            return False
    listPos.append((curX, curY))
    if len(listPos) == C:
        for curX, curY in listPos:
            Map[curX][curY] = 'o'
        return True
    else:
        return False


RET = 0
for i in range(R):
    if putPipeLine(i):
        RET += 1

print(RET)

for i in range(R):
    print(Map[i])
