import sys
import copy

input = sys.stdin.readline

TOP, RIGHT, BOTTOM, LEFT = 0, 1, 2, 3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(count):
    global board

    if count == 5:
        setMaxBlock(board)
        return

    for i in range(4):
        prevBoard = copy.deepcopy(board)
        setBoard(i)
        dfs(count+1)
        board = prevBoard


def setBoard(direction):
    global board
    reversedDirection = (direction+2) % 4

    for index in range(N):
        if direction == TOP:
            startX, startY = 0, index
        elif direction == RIGHT:
            startX, startY = index, N-1
        elif direction == BOTTOM:
            startX, startY = N-1, index
        elif direction == LEFT:
            startX, startY = index, 0

        # push numbers in stack
        curX, curY = startX, startY
        stack = []
        while 0 <= curX <= N-1 and 0 <= curY <= N-1:
            curNumber = board[curX][curY]
            if curNumber != 0:
                stack.append(curNumber)

            curX += dx[reversedDirection]
            curY += dy[reversedDirection]

        # merge
        i = 0
        while i < len(stack)-1:
            if stack[i] == stack[i+1]:
                stack[i] *= 2
                del stack[i+1]
            i += 1

        # align
        curX, curY = startX, startY
        while 0 <= curX <= N-1 and 0 <= curY <= N-1:
            if len(stack) >= 1:
                board[curX][curY] = stack.pop(0)
            else:
                board[curX][curY] = 0

            curX += dx[reversedDirection]
            curY += dy[reversedDirection]


def setMaxBlock(board):
    global maxBlock

    for i in range(N):
        for j in range(N):
            maxBlock = max(maxBlock, board[i][j])


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]


maxBlock = 0
dfs(0)
print(maxBlock)
