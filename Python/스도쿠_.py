import sys
input = sys.stdin.readline


def getZeroPositions():
    zeroPositions = []

    for i in range(9):
        for j in range(9):
            if nums[i][j] == 0:
                zeroPositions.append((i, j))

    return zeroPositions


def dfs(zeroIndex):
    if zeroLength <= zeroIndex:
        return True

    x, y = zeroPositions[zeroIndex]
    isAvailableNumbers = getIsAvailableNumbers(x, y)

    for n in range(1, 10):
        if isAvailableNumbers[n]:
            nums[x][y] = n
            if dfs(zeroIndex + 1):
                return True
            nums[x][y] = 0

    return False


def getIsAvailableNumbers(x, y):
    isAvailableNumbers = [True]*10

    sectorX = x//3
    sectorY = y//3

    # Sector
    for i in range(3):
        for j in range(3):
            isAvailableNumbers[nums[sectorX*3 + i][sectorY*3 + j]] = False

    # 가로
    for i in range(9):
        isAvailableNumbers[nums[i][y]] = False

    # 세로
    for j in range(9):
        isAvailableNumbers[nums[x][j]] = False

    return isAvailableNumbers


if __name__ == '__main__':
    # 입력
    nums = []
    for _ in range(9):
        curNums = []
        for c in input().rstrip():
            curNums.append(int(c))
        nums.append(curNums)

    # 메인 로직
    zeroPositions = getZeroPositions()
    zeroLength = len(zeroPositions)

    dfs(0)

    # 출력
    for i in range(9):
        for j in range(9):
            print(nums[i][j], end="")
        print()
