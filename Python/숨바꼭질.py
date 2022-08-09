N, K = map(int, input().split())

isVisited = [False]*100001
todo = [N]
RET = -1
while todo:
    nextTodo = []
    for curPos in todo:
        if curPos==K:
            nextTodo=[]
            break
        idx = curPos-1
        if idx>=0 and not isVisited[idx]:
            isVisited[idx]=True
            nextTodo.append(idx)
        idx = curPos+1
        if idx<=100000 and not isVisited[idx]:
            isVisited[idx]=True
            nextTodo.append(idx)
        idx = curPos*2
        if idx<=100000 and not isVisited[idx]:
            isVisited[idx]=True
            nextTodo.append(idx)
    todo = nextTodo
    RET+=1
print(RET)