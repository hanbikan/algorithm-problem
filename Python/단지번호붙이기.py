import sys
read = sys.stdin.readline
N=int(read())
Map = [[0]*N for _ in range(N)]

for i in range(N):
    line = read().strip()
    for j, b in enumerate(line):
        Map[i][j] = int(b)

def dfs(x, y):
    global Map
    global curApt
    curApt += 1
    Map[x][y]=0
    if x-1>=0:
        if Map[x-1][y]==1:
            dfs(x-1, y)
    if y-1>=0:
        if Map[x][y-1]==1:
            dfs(x, y-1)
    if x+1<=N-1:
        if Map[x+1][y]==1:
            dfs(x+1, y)
    if y+1<=N-1:
        if Map[x][y+1]==1:
            dfs(x, y+1)

amountComplex=0
listAmountsApt = []
for i in range(N):
    for j in range(N):
        if Map[i][j] == 1:
            curApt = 0
            amountComplex+=1
            dfs(i, j)
            listAmountsApt.append(curApt)
print(amountComplex)
listAmountsApt = sorted(listAmountsApt)
for cur in listAmountsApt: print(cur)