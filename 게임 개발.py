import sys
read = sys.stdin.readline

def recur(idx):
    if DP1[idx]==True: return
    for i in range(1, len(Input[idx])-1):
        recur(Input[idx][i]-1)
    if not IsPossibleToBuild(idx): runQ()
    q.append(idx)
    DP1[idx] = True

def IsPossibleToBuild(idx):
    for i in range(1, len(Input[idx])-1):
        if DP2[Input[idx][i]-1]==False:
            return False
    return True

def runQ():
    maxTime = 0
    for i in range(len(q)):
        if maxTime<Input[q[i]][0]: maxTime=Input[q[i]][0]
    print(maxTime)
    for i in range(len(q)): del q[0]
#N=5
#Input = [[10,-1],[10,1,4,5,-1],[4,1,-1],[4,3,1,-1],[3,3,-1]]
Input=[]
N = int(input())
for i in range(N):
    Input.append(list(map(int,read().strip().split())))
for idx in range(N):
    RET=0
    DP1 = [False for i in range(N)]
    DP2 = [False for i in range(N)]
    q = []
    recur(idx)
    runQ()

    print(RET)
    print()