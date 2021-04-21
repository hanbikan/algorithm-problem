import sys
from itertools import combinations
input = sys.stdin.readline


def getAvailableDeskCounts():
    availableDeskCounts = []

    for i in range(M):
        curCount = 0
        for j in range(N):
            if curClassroom[j][i] == '.':
                curCount += 1

        availableDeskCounts.append(curCount)

    return availableDeskCounts


def getSelectionCount(availableDeskCounts):
    global curClassroom
    getSelectionCount = 0

    dp = [availableDeskCounts[i] for i in range(M)]
    dpLog = []
    dpLog.append(-1)
    if M >= 2:
        dpLog.append(-1)
    if M >= 3:
        dp[2] += dp[0]
        dpLog.append(0)

    # dp 및 dpLog 구하기
    for i in range(3, M):
        if dp[i-2] > dp[i-3]:
            dp[i] += dp[i-2]
            dpLog.append(i-2)
        else:
            dp[i] += dp[i-3]
            dpLog.append(i-3)

    if M == 1:
        seletedLineIndexes = [0]
    else:
        # seletedLineIndexes: 위 dp를 기준으로 최댓값을 얻을 수 있는 라인들 인덱스의 집합
        if dp[-1] > dp[-2]:
            seletedLineIndexes = getSeletedLineIndexes(dpLog, M-1)
        else:
            seletedLineIndexes = getSeletedLineIndexes(dpLog, M-2)

        # dpTrace의 라인은 모두 학생을 배치한다.
    for i in seletedLineIndexes:
        for j in range(N):
            if curClassroom[j][i] == '.':
                # y는 해당 좌표에 학생이 배치됐다는 뜻
                getSelectionCount += 1
                curClassroom[j][i] = 'y'

    return getSelectionCount


# dpLog를 따라가면서 dpTrace를 리턴
def getSeletedLineIndexes(dpLog, index):
    seletedLineIndexes = [index]

    curIndex = index
    while dpLog[curIndex] != -1:
        seletedLineIndexes.append(dpLog[curIndex])
        curIndex = dpLog[curIndex]

    return seletedLineIndexes


# x, y 좌표에 배치할 수 있는지 확인
def checkIfAvailablePosition(x, y):
    global curClassroom

    dx = [0, -1, -1, 0, 1, 1]
    dy = [-1, -1, 1, 1, -1, 1]
    for i in range(6):
        curX, curY = x+dx[i], y+dy[i]

        if 0 <= curX <= N-1 and 0 <= curY <= M-1:
            if curClassroom[curX][curY] == 'y':
                return False

    return True


def getMaxSelection():
    global curClassroom

    allAvailablePositions = []
    for i in range(M):
        allAvailablePositions += getAvailablePositions(i)

    for i in range(len(allAvailablePositions), 0, -1):
        curCombinationList = list(combinations(allAvailablePositions, i))
        for curPositions in curCombinationList:
            isAvailableClassroom = True

            for pos in curPositions:
                curClassroom[pos[0]][pos[1]] = 'y'
                if not checkIfAvailablePosition(pos[0], pos[1]):
                    isAvailableClassroom = False
                    break

            if isAvailableClassroom:
                return i

            for pos in curPositions:
                curClassroom[pos[0]][pos[1]] = '.'

    return 0


def getAvailablePositions(lineIndex):
    availablePositions = []

    for i in range(N):
        if curClassroom[i][lineIndex] == '.':
            if checkIfAvailablePosition(i, lineIndex):
                availablePositions.append((i, lineIndex))

    return availablePositions


N, M = -1, -1
curClassroom = []
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    curClassroom = []
    for _ in range(N):
        curInputLine = input().rstrip()

        curLine = []
        for c in curInputLine:
            curLine.append(c)

        curClassroom.append(curLine)

    curAvailableDeskCounts = getAvailableDeskCounts()
    print(getSelectionCount(curAvailableDeskCounts)+getMaxSelection())
