import sys
import copy
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def getCyclePositions():
    airCleanerTopX = -1
    airCleanerBottomX = -1

    for i in range(R):
        if fineDusts[i][0] == -1:
            airCleanerTopX = i
            airCleanerBottomX = i + 1
            break

    topCyclePositions = [(airCleanerTopX, j) for j in range(1, C)] + [(i, C - 1) for i in range(
        airCleanerTopX-1, 0, -1)] + [(0, j) for j in range(C-1, -1, -1)] + [(i, 0) for i in range(airCleanerTopX)]

    bottomCyclePositions = [(airCleanerBottomX, j) for j in range(1, C)] + [(i, C - 1) for i in range(
        airCleanerBottomX+1, R-1)] + [(R-1, j) for j in range(C-1, -1, -1)] + [(i, 0) for i in range(R-2, airCleanerBottomX, -1)]

    return topCyclePositions, bottomCyclePositions


def getNextFineDusts():
    nextFineDusts = copy.deepcopy(fineDusts)

    # diffuse
    for x in range(R):
        for y in range(C):
            cur = fineDusts[x][y]
            if cur <= 4:
                continue

            for i in range(4):
                adjX, adjY = x + dx[i], y + dy[i]

                if 0 <= adjX <= R-1 and 0 <= adjY <= C-1 and nextFineDusts[adjX][adjY] != -1:
                    nextFineDusts[adjX][adjY] += cur // 5
                    nextFineDusts[x][y] -= cur // 5

    # cycle
    for i in range(topCycleLength-1, 0, -1):
        prevX, prevY = topCyclePositions[i-1]
        x, y = topCyclePositions[i]
        nextFineDusts[x][y] = nextFineDusts[prevX][prevY]
    nextFineDusts[topCyclePositions[0][0]][topCyclePositions[0][1]] = 0

    for i in range(bottomCycleLength-1, 0, -1):
        prevX, prevY = bottomCyclePositions[i-1]
        x, y = bottomCyclePositions[i]
        nextFineDusts[x][y] = nextFineDusts[prevX][prevY]
    nextFineDusts[bottomCyclePositions[0][0]][bottomCyclePositions[0][1]] = 0

    return nextFineDusts


if __name__ == '__main__':
    # 입력
    R, C, T = map(int, input().split())
    fineDusts = [list(map(int, input().split())) for _ in range(R)]

    # 처리
    topCyclePositions, bottomCyclePositions = getCyclePositions()
    topCycleLength, bottomCycleLength = len(
        topCyclePositions), len(bottomCyclePositions)

    for i in range(T):
        fineDusts = getNextFineDusts()

    # 출력
    print(sum(sum(fineDusts[i]) for i in range(R)) + 2)
