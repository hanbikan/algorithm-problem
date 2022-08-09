def dfs(x, y, cntMove):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    global RET
    RET = max(RET, cntMove)

    for i in range(4):
        curX = x + dx[i]
        curY = y + dy[i]

        if (0 <= curX <= R-1) and (0 <= curY <= C-1):
            if(isVisitedAlphabet[getNumberOfAlphabet(board[curX][curY])] == False):
                isVisitedAlphabet[getNumberOfAlphabet(
                    board[curX][curY])] = True
                dfs(curX, curY, cntMove+1)
                isVisitedAlphabet[getNumberOfAlphabet(
                    board[curX][curY])] = False


def getNumberOfAlphabet(char):
    return ord(char)-ord('A')


R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

isVisitedAlphabet = [False]*26
isVisitedAlphabet[getNumberOfAlphabet(board[0][0])] = True
RET = 1
dfs(0, 0, RET)
print(RET)
