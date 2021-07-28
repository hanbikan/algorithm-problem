import sys
import itertools

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def getMinChickenDistance():
    minChickenDistance = float('inf')

    # 치킨집 위치 & 치킨집 -> 집까지 거리 저장
    chickenPositions = []

    for i in range(N):
        for j in range(N):
            if city[i][j] == 2:
                chickenPositions.append((i, j))
                setDistanceChickenToHouse((i, j))

    # 살아남을 지점들 선택
    cases = list(itertools.combinations(
        chickenPositions, M))

    for chickens in cases:
        curMinDist = {}

        # 각 치킨집 -> house
        for pos in chickens:
            for p, d in distanceChickedToHouse[pos].items():
                if curMinDist.get(p):
                    curMinDist[p] = min(curMinDist[p], d)
                else:
                    curMinDist[p] = d

        minChickenDistance = min(minChickenDistance, sum(curMinDist.values()))

    return minChickenDistance


def setDistanceChickenToHouse(startPos):
    curDist = 0
    isVisited = [[False]*N for _ in range(N)]
    isVisited[startPos[0]][startPos[1]] = True
    todo = [startPos]

    while todo:
        curDist += 1
        nextTodo = []

        for x, y in todo:
            for i in range(4):
                nextX, nextY = x + dx[i], y + dy[i]

                if nextX < 0 or nextX > N-1 or nextY < 0 or nextY > N-1:
                    continue

                if isVisited[nextX][nextY] == False:
                    if city[nextX][nextY] == 1:
                        if distanceChickedToHouse.get(startPos):
                            distanceChickedToHouse[startPos][(
                                nextX, nextY)] = curDist
                        else:
                            distanceChickedToHouse[startPos] = {
                                (nextX, nextY): curDist}

                    isVisited[nextX][nextY] = True
                    nextTodo.append((nextX, nextY))

        todo = nextTodo


if __name__ == '__main__':
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]

    distanceChickedToHouse = {}

    print(getMinChickenDistance())
