import sys
input = sys.stdin.readline


def getBlankPositions():
    blankPositions = []

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                blankPositions.append([i, j])

    return blankPositions


def dfs(blankIndex):
    global board

    if blankIndex == len(blankPositions):
        if isBoardAvailable():
            printBoard()
            return True
        else:
            return False

    blankX, blankY = map(int, blankPositions[blankIndex])
    possibleNumbers = getPossibleNumbers(blankX, blankY)

    for n in possibleNumbers:
        board[blankX][blankY] = n
        if dfs(blankIndex+1) == True:
            return True
        board[blankX][blankY] = 0


def getPossibleNumbers(x, y):
    isPossibleNumber = [True]*10

    # 가로 세로
    for i in range(9):
        isPossibleNumber[board[x][i]] = False
        isPossibleNumber[board[i][y]] = False

    # 섹터
    lineX, lineY = x//3, y//3
    for i in range(3):
        for j in range(3):
            curX, curY = 3*lineX+i, 3*lineY+j
            isPossibleNumber[board[curX][curY]] = False

    possibleNumbers = []
    for i in range(1, 10):
        if isPossibleNumber[i]:
            possibleNumbers.append(i)

    return possibleNumbers


def isBoardAvailable():
    # 가로
    for i in range(9):
        isNumbersAppeared = [False]*10
        for j in range(9):
            if isNumbersAppeared[board[i][j]] != False:
                return False
            isNumbersAppeared[board[i][j]] = True

    # 세로
    for i in range(9):
        isNumbersAppeared = [False]*10
        for j in range(9):
            if isNumbersAppeared[board[j][i]] != False:
                return False
            isNumbersAppeared[board[j][i]] = True

    # 섹터
    for i in range(3):
        for j in range(3):
            lineX, lineY = i, j
            isNumbersAppeared = [False]*10

            for k in range(3):
                for l in range(3):
                    curX, curY = 3*lineX+k, 3*lineY+l
                    if isNumbersAppeared[board[curX][curY]] != False:
                        return False
                    isNumbersAppeared[board[curX][curY]] = True

    return True


def printBoard():
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()


board = [list(map(int, input().split())) for _ in range(9)]

blankPositions = getBlankPositions()
dfs(0)
