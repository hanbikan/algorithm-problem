import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def setIsDoorAvailable(keys):
    if keys != "0":
        for c in keys:
            isDoorAvailable[convertAlphabetToNumber(c)] = True


def setAvailableDocumentCount():
    outerPositions = \
        [(0, j) for j in range(W)] + [(H-1, j) for j in range(W)] + \
        [(i, 0) for i in range(1, H-1)] + [(i, W-1) for i in range(1, H-1)]

    for x, y in outerPositions:
        if isPositionReachable((x, y)):
            searchForSector((x, y))


def searchForSector(pos):
    todo = [pos]

    while todo:
        x, y = todo.pop(0)

        if isVisited[x][y] == False:
            todo += searchAndGetNextPositions((x, y))


def searchAndGetNextPositions(pos):
    global availableDocumentCount

    todo = [pos]
    unlockedDoorIndices = []
    isVisited[pos[0]][pos[1]] = True

    while todo:
        x, y = todo.pop(0)
        c = buildingMap[x][y]
        cIndex = convertAlphabetToNumber(c)

        # 키를 얻음으로써 문을 개방함
        if 'a' <= c <= 'z':
            if isDoorAvailable[cIndex] == False:
                isDoorAvailable[cIndex] = True
                unlockedDoorIndices.append(cIndex)
        # 문서
        elif c == '$':
            availableDocumentCount += 1

        # 인접 노드 추가
        for i in range(4):
            nextX, nextY = x + dx[i], y + dy[i]

            if 0 <= nextX <= H-1 and 0 <= nextY <= W-1:
                if isPositionReachable((nextX, nextY)):
                    todo.append((nextX, nextY))
                    isVisited[nextX][nextY] = True

    # 이번 탐색으로 열린 문들 중에, 이전에 접근 실패했던 인접 좌표들을 반환함
    nextPositions = []
    for i in unlockedDoorIndices:
        for x, y in adjacentUnavailableDoorPositions[i]:
            nextPositions.append((x, y))

    return nextPositions


def convertAlphabetToNumber(c):
    if 'a' <= c <= 'z':
        return ord(c)-ord('a')
    elif 'A' <= c <= 'Z':
        return ord(c)-ord('A')
    else:
        return -1


def isPositionReachable(pos):
    x, y = pos
    c = buildingMap[x][y]
    cIndex = convertAlphabetToNumber(c)

    if (isVisited[x][y] == False) and (c == '.' or c == '$' or ('a' <= c <= 'z') or ('A' <= c <= 'Z' and isDoorAvailable[cIndex])):
        return True
    else:
        if 'A' <= c <= 'Z' and isDoorAvailable[cIndex] == False:
            adjacentUnavailableDoorPositions[cIndex].append((x, y))

        return False


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        # 입력
        H, W = map(int, input().split())
        buildingMap = [str(input().rstrip()) for _ in range(H)]
        keys = str(input().rstrip())

        # 탐색을 위한 변수 초기화
        isDoorAvailable = [False]*26
        setIsDoorAvailable(keys)

        isVisited = [[False]*W for _ in range(H)]
        adjacentUnavailableDoorPositions = [[] for _ in range(26)]
        
        availableDocumentCount = 0

        # 탐색
        setAvailableDocumentCount()

        # 출력
        print(availableDocumentCount)
