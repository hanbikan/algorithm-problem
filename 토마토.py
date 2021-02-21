RAW, RIPE = 0, 1
M, N = map(int, input().split())
MAP = []
for i in range(N):
    MAP.append(list(map(int, input().split())))

TODO=[]
amountRaw = 0
for i in range(len(MAP)):
    for j in range(len(MAP[i])):
        if MAP[i][j] == RIPE: TODO.append([i,j]) # 1. TODO에 1인 것들 넣기
        elif MAP[i][j] == RAW: amountRaw += 1 # 2. 0 갯수 세기(모두 익었는지 확인할 때 사용)

RET=-1
while TODO:
    RET+=1
    nextTODO = []
    for curPos in TODO:
        x, y = curPos[0], curPos[1]
        if x-1>=0 and MAP[x-1][y]==RAW:
            nextTODO.append([x-1, y])
            MAP[x-1][y] = RIPE
            amountRaw -= 1
        if y-1>=0 and MAP[x][y-1]==RAW:
            nextTODO.append([x, y-1])
            MAP[x][y-1] = RIPE
            amountRaw -= 1
        if x+1<N and MAP[x+1][y]==RAW:
            nextTODO.append([x+1, y])
            MAP[x+1][y] = RIPE
            amountRaw -= 1
        if y+1<M and MAP[x][y+1]==RAW:
            nextTODO.append([x, y+1])
            MAP[x][y+1] = RIPE
            amountRaw -= 1
    TODO = nextTODO
if amountRaw == 0: print(RET)
else: print(-1)