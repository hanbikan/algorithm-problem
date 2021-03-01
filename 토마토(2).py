X, Y, Z = 0, 1, 2 #for tomatoes
M, N, H = map(int, input().split())
tomatoes = []
todo = []
cntRaw = 0
for i in range(H):
    curSquare = []
    for j in range(N):
        curSquare.append(list(map(int, input().split())))
        for k in range(M):
            if curSquare[j][k]==1: todo.append([i, j, k])
            elif curSquare[j][k]==0: cntRaw+=1
    tomatoes.append(curSquare)

cntTry = -1
while todo:
    nextTodo = []
    for curPos in todo:
        x, y, z = curPos[X], curPos[Y], curPos[Z]-1
        if z>=0 and tomatoes[x][y][z]==0:
            nextTodo.append([x, y, z])
            tomatoes[x][y][z] = 1
            cntRaw-=1
        x, y, z = curPos[X], curPos[Y]-1, curPos[Z]
        if y>=0 and tomatoes[x][y][z]==0:
            nextTodo.append([x, y, z])
            tomatoes[x][y][z] = 1
            cntRaw-=1
        x, y, z = curPos[X]-1, curPos[Y], curPos[Z]
        if x>=0 and tomatoes[x][y][z]==0:
            nextTodo.append([x, y, z])
            tomatoes[x][y][z] = 1
            cntRaw-=1
        x, y, z = curPos[X], curPos[Y], curPos[Z]+1
        if z<=M-1 and tomatoes[x][y][z]==0:
            nextTodo.append([x, y, z])
            tomatoes[x][y][z] = 1
            cntRaw-=1
        x, y, z = curPos[X], curPos[Y]+1, curPos[Z]
        if y<=N-1 and tomatoes[x][y][z]==0:
            nextTodo.append([x, y, z])
            tomatoes[x][y][z] = 1
            cntRaw-=1
        x, y, z = curPos[X]+1, curPos[Y], curPos[Z]
        if x<=H-1 and tomatoes[x][y][z]==0:
            nextTodo.append([x, y, z])
            tomatoes[x][y][z] = 1
            cntRaw-=1
    todo=nextTodo
    cntTry+=1
if cntRaw==0: print(cntTry)
else: print(-1)