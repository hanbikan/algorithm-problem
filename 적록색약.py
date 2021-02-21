import sys
sys.setrecursionlimit(10000)

N = int(input())
pic=[[] for _ in range(N)]
picForRG=[[] for _ in range(N)]

for i in range(N):
    curLine = input()
    for j in range(N):
        pic[i].append(curLine[j])
        if curLine[j]=='G':
            picForRG[i].append('R')
        else:
            picForRG[i].append(curLine[j])
            
def bfs(x, y, Map, visitedNum):
    global N, visited
    visited[visitedNum][x][y]=True
    if x-1>=0 and Map[x-1][y]==Map[x][y] and visited[visitedNum][x-1][y]==False:
        bfs(x-1, y, Map, visitedNum)
    if y-1>=0 and Map[x][y-1]==Map[x][y] and visited[visitedNum][x][y-1]==False:
        bfs(x, y-1, Map, visitedNum)
    if x+1<=N-1 and Map[x+1][y]==Map[x][y] and visited[visitedNum][x+1][y]==False:
        bfs(x+1, y, Map, visitedNum)
    if y+1<=N-1 and Map[x][y+1]==Map[x][y] and visited[visitedNum][x][y+1]==False:
        bfs(x, y+1, Map, visitedNum)
        
visited = [[[False]*N for _ in range(N)] for _ in range(2)]
RET1, RET2 = 0, 0
for i in range(N):
    for j in range(N):
        if visited[0][i][j]==False:
            RET1+=1
            bfs(i, j, pic, 0)
        if visited[1][i][j]==False:
            RET2+=1
            bfs(i, j, picForRG, 1)
            
print(RET1, RET2)