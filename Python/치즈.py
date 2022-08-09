import sys

input = sys.stdin.readline
AIR, CHEESE = 0, 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def getMinTime():
    minTime = 0

    while meltCheese():
        minTime += 1

    return minTime


def meltCheese():
    outerPositions = [(i, 0) for i in range(N)] + [(i, M-1) for i in range(N)] +\
        [(0, j) for j in range(1, M-1)] + [(N-1, j) for j in range(1, M-1)]
    isVisited = [[False]*M for _ in range(N)]

    for ox, oy in outerPositions:
        if isVisited[ox][oy] == True:
            continue

        isVisited[ox][oy] = True

        if grid[ox][oy] == AIR:
            todo = [(ox, oy)]

            while todo:
                x, y = todo.pop(0)

                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]

                    if 0 <= nx <= N-1 and 0 <= ny <= M-1:
                        adj = grid[nx][ny]

                        if isVisited[nx][ny] == False and adj == AIR:
                            todo.append((nx, ny))
                            isVisited[nx][ny] = True
                        elif adj >= CHEESE:
                            grid[nx][ny] += 1
        else:
            grid[ox][oy] += 1

    # 치즈 녹이기, 치즈 1로 초기화
    flag = False
    for i in range(N):
        for j in range(M):
            n = grid[i][j]

            if n >= 3:
                grid[i][j] = 0
                flag = True
            elif n == 2:
                grid[i][j] = 1

    return flag


if __name__ == '__main__':
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    minTime = getMinTime()
    print(minTime)
