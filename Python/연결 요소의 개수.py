import sys
read=sys.stdin.readline
sys.setrecursionlimit(30000)

def dfs(linked, dest):
    global isVisited
    
    isVisited[dest] = 1
    if not linked.get(dest): return

    for s in linked[dest]:
        if not isVisited[s]:
            dfs(linked, s)

N, M = map(int, read().strip().split())
u, v = [], []
linked = {}
isVisited = [0] * 1001

for i in range(M):
    uInput, vInput = map(int, read().strip().split())
    u.append(uInput)
    v.append(vInput)
    if not linked.get(uInput): linked[uInput] = [vInput]
    else: linked[uInput].append(vInput)
    if not linked.get(vInput): linked[vInput] = [uInput]
    else: linked[vInput].append(uInput)

RET=0
for i in range(1, N+1):
    if not isVisited[i]:
        dfs(linked, i)
        RET+=1
print(RET)