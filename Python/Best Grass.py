import sys
read = sys.stdin.readline

def searchAdjacent(listAdjacent):
    for i in range(len(listAdjacent)):
        x = listAdjacent[i]//C
        y = listAdjacent[i]%C
        if lines[x][y] == '#':
            graph[listAdjacent[i]] = []

R, C = map(int, read().strip().split())
lines=[]
for i in range(R):
    line = []
    tmp = read()
    for char in tmp:
        line.append(char)
    lines.append(line)
    
graph = {i:[] for i in range(R*C)}

graphIdx = 0
for i in range(R):
    for j in range(C):
        if i-1>=0:
            graph[graphIdx].append(graphIdx-C)
        if j-1>=0:
            graph[graphIdx].append(graphIdx-1)
        if i+1<=R-1:
            graph[graphIdx].append(graphIdx+C)
        if j+1<=C-1:
            graph[graphIdx].append(graphIdx+1)
        graphIdx+=1

graphIdx=0
RET = 0
for i in range(R):
    for j in range(C):
        if lines[i][j]=='#' and graph[graphIdx]!=[]:
            searchAdjacent(graph[graphIdx])
            RET += 1
        graphIdx+=1
print(RET)