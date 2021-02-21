RET=0
N=7
tasks=[[5,0],[1,1,1],[3,1,2],[6,1,1],[1,2,2,4],[8,2,2,4],[4,3,3,5,6]]
DP = [[] for i in range(N)]
for i in range(len(tasks)):
    for j in range(2, len(tasks[i])):
        DP[tasks[i][j]-1].append(i)

todo=[0]
while True:
    print(todo, tasks)
    if todo==[]: break
    maxTime=0
    nextTodo=[]
    for i in range(len(todo)):
        if len(todo)==2: maxTime = max(maxTime, tasks[todo[i]][0])
        for j in range(len(DP[todo[i]])):
            for k in range(2, len(tasks[DP[todo[i]][j]])):
                if tasks[DP[todo[i]][j]][k]==todo[i]: del tasks[DP[todo[i]][j]][k]
            nextTodo.append(DP[todo[i]][j])
    todo = nextTodo
    RET+=maxTime

print(maxTime)