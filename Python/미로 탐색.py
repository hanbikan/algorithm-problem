import sys
read = sys.stdin.readline

def bfs():
    todo = setDPAndGetNextPos(0,0,0,0)
    while todo:
        nextTodo = []
        for [x, y, prevX, prevY] in todo:
            nextTodo += setDPAndGetNextPos(x, y, prevX, prevY)
        todo = nextTodo
        
def setDPAndGetNextPos(x, y, prevX, prevY):
    global dp, MAP, N, M
    RET = []

    if dp[x][y]==0: dp[x][y] = dp[prevX][prevY]+1
    else:
        if(dp[x][y] <= dp[prevX][prevY]+1): return RET
        else: dp[x][y] = dp[prevX][prevY]+1

    if x-1>=0 and MAP[x-1][y]==1: RET.append([x-1, y, x, y])
    if y-1>=0 and MAP[x][y-1]==1: RET.append([x, y-1, x, y])
    if x+1<=N-1 and MAP[x+1][y]==1: RET.append([x+1, y, x, y])
    if y+1<=M-1 and MAP[x][y+1]==1: RET.append([x, y+1, x, y])

    return RET

N, M = map(int, read().strip().split())
dp = [[0]*M for _ in range(N)]
MAP = []
for i in range(N):
    toAppended = []
    curLine = input()
    for j in range(len(curLine)):
        toAppended.append(int(curLine[j]))
    MAP.append(toAppended)

bfs()
print(dp[-1][-1])