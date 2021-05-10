import sys
import copy
input = sys.stdin.readline

TOP, RIGHT, BOTTOM, LEFT = 0, 1, 2, 3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    global curMap, curRedPos, curBluePos

    todo = [[map, redPos, bluePos, 1]]
    # 2개의 구슬의 위치를 기록하여 중복을 허용하지 않도록 함
    ballRecords = [[redPos, bluePos]]

    while todo:
        curOriginalMap, curOriginalRedPos, curOriginalBluePos, curCount = todo.pop(
            0)
        if curCount >= 11:
            return -1

        for j in range(4):
            # curMap, curRedPos, curBluePos를 새로 만들면, 하위 함수들은 이 세 변수들을 수정함
            curMap = copy.deepcopy(curOriginalMap)
            curRedPos = copy.deepcopy(curOriginalRedPos)
            curBluePos = copy.deepcopy(curOriginalBluePos)

            # j에 따라 맵 기울이기... 이 때 curMap, curRedPos, curBluePos 모두 변함
            tiltBoard(j)

            # [-1, -1]의 의미는 O를 만나 떨어졌다는 것임
            if curBluePos == [-1, -1]:
                continue
            elif curRedPos == [-1, -1]:
                return curCount  # bfs이므로 바로 return 함
            else:
                # curRedPos, curBluePos의 값은 중복되면 안 됨
                if [curRedPos, curBluePos] in ballRecords:
                    continue

                # [변화된 curMap, curRedPos, curBluePos, 그리고 이동횟수+1]를
                todo.append([curMap, curRedPos, curBluePos, curCount+1])
                ballRecords.append([curRedPos, curBluePos])

    return -1


def tiltBoard(direction):
    global curMap, curRedPos, curBluePos

    # Red와 Blue 두 개에 대해서 tiltAndGetCollapsed를 수행해야하는데 순서를 정해줌
    # 순서 정하는 이유: [. R . B]에서 왼쪽으로 기울인다고 하자. B, R 순서로 기울이면 [R . B .]가 됨
    todo = [curRedPos, curBluePos]
    if direction == TOP:
        if curRedPos[0] > curBluePos[0]:
            todo = [curBluePos, curRedPos]
    elif direction == RIGHT:
        if curRedPos[1] < curBluePos[1]:
            todo = [curBluePos, curRedPos]
    elif direction == BOTTOM:
        if curRedPos[0] < curBluePos[0]:
            todo = [curBluePos, curRedPos]
    elif direction == LEFT:
        if curRedPos[1] > curBluePos[1]:
            todo = [curBluePos, curRedPos]

    # 정해진 순서에 따라서 각 구슬을 기울여줌
    for curPos in todo:
        isR = curPos == curRedPos

        if(tiltAndGetCollapsed(direction, curPos) == 'O'):
            curMap[curRedPos[0]][curRedPos[1]] = '.'

            # [-1, -1] 의미: 구슬이 구멍으로 떨어짐
            if isR:
                curRedPos = [-1, -1]
            else:
                curBluePos = [-1, -1]


def tiltAndGetCollapsed(direction, pos):
    curPos = [pos[0], pos[1]]
    while 0 <= curPos[0] <= N-1 and 0 <= curPos[1] <= M-1:
        curPos[0] += dx[direction]
        curPos[1] += dy[direction]

        if curMap[curPos[0]][curPos[1]] != '.':
            moveBall(pos, [curPos[0]-dx[direction], curPos[1]-dy[direction]])
            return curMap[curPos[0]][curPos[1]]


def moveBall(prevPos, nextPos):
    if prevPos == nextPos:
        return

    global curMap, curRedPos, curBluePos

    if prevPos == curRedPos:
        curRedPos = nextPos
    elif prevPos == curBluePos:
        curBluePos = nextPos

    curMap[nextPos[0]][nextPos[1]] = curMap[prevPos[0]][prevPos[1]]
    curMap[prevPos[0]][prevPos[1]] = '.'


N, M = map(int, input().split())
map = []
curMap = None
curRedPos = [-1, -1]
curBluePos = [-1, -1]

for i in range(N):
    curInput = input().rstrip()
    curLine = []
    for j in range(M):
        c = curInput[j]
        if c == 'R':
            redPos = [i, j]
        elif c == 'B':
            bluePos = [i, j]
        curLine.append(c)
    map.append(curLine)

print(bfs())
