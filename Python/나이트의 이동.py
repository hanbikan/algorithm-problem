import sys
input = sys.stdin.readline


def getNextPos(x, y):
    global isVisited
    RET = []
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]

    for i in range(8):
        curX, curY = x+dx[i], y+dy[i]
        if 0 <= curX <= I-1 and 0 <= curY <= I-1:
            if isVisited[curX][curY] == False and ((posEnd[X]-curX > 0 and dx[i] > 0) or (posEnd[X]-curX < 0 and dx[i] < 0) or (posEnd[X]-2 <= curX <= posEnd[X]+2)) and ((posEnd[Y]-curY > 0 and dy[i] > 0) or (posEnd[Y]-curY < 0 and dy[i] < 0) or (posEnd[Y]-2 <= curY <= posEnd[Y]+2)):
                RET.append([curX, curY])
                isVisited[curX][curY] = True
    return RET


X, Y = 0, 1
T = int(input())
for _ in range(T):
    I = int(input())
    posStart = list(map(int, input().split()))
    posEnd = list(map(int, input().split()))
    if posStart == posEnd:
        print(0)
        continue

    isVisited = [[False]*I for _ in range(I)]
    isVisited[posStart[X]][posStart[Y]] = True
    todo = getNextPos(posStart[X], posStart[Y])
    cntMove = 0
    while todo:
        cntMove += 1
        nextTodo = []
        for curPos in todo:
            if curPos == posEnd:
                nextTodo = []
                break
            nextTodo += getNextPos(curPos[X], curPos[Y])
        todo = nextTodo
    print(cntMove)
