import sys
read = sys.stdin.readline

def getMaxTimeFromZ2(idx):
    RET = 0
    if Z2.get(idx):
        times=[]
        for i in range(len(Z2[idx])):
            times.append(D[Z2[idx][i]])
        RET += max(times)
    return RET

T=int(read())
for I in range(T):
    N, K = map(int, read().strip().split())
    dp = [0]*N
    D=list(map(int, read().strip().split()))
    X, Y = [], []
    Z1, Z2 = {}, {}
    for J in range(K):
        x, y = map(int, read().strip().split())
        X.append(x)
        Y.append(y)
        if not Z1.get(x-1):
            Z1[x-1]=[y-1]
        else:
            Z1[x-1].append(y-1)
        if not Z2.get(y-1):
            Z2[y-1]=[x-1]
        else:
            Z2[y-1].append(x-1)
    for i in range(N):
        if not Z2.get(i):
            todo = [i]
            break
    W=int(read())
    while todo!=[]:
        print(todo)
        nexttodo = []
        for i in range(len(todo)):
            dp[i] += getMaxTimeFromZ2(todo[i]) + D[i]
            if Z1.get(todo[i]):
                nexttodo += Z1[todo[i]]
        todo = nexttodo
    print(dp)