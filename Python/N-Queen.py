import sys
input = sys.stdin.readline


def setUnattackableCountRecursively(index):
    if index == N-1:
        for i in range(N):
            if isAvailable[i][index] == 0:
                global unattackableCount
                unattackableCount += 1
    else:
        for i in range(N):
            if isAvailable[i][index] == 0:
                setIsAvailable(1, i, index)
                setUnattackableCountRecursively(index+1)
                setIsAvailable(-1, i, index)


def setIsAvailable(num, x, y):
    # →
    curX, curY = x, y+1
    while curY <= N-1:
        isAvailable[curX][curY] += num

        curY += 1

    # ↗
    curX, curY = x-1, y+1
    while curX >= 0 and curY <= N-1:
        isAvailable[curX][curY] += num

        curX -= 1
        curY += 1

    # ↘
    curX, curY = x+1, y+1
    while curX <= N-1 and curY <= N-1:
        isAvailable[curX][curY] += num

        curX += 1
        curY += 1


if __name__ == '__main__':
    N = int(input())

    isAvailable = [[0]*N for _ in range(N)]

    unattackableCount = 0
    setUnattackableCountRecursively(0)
    print(unattackableCount)
