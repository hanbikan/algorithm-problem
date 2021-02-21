import sys
read = sys.stdin.readline

N = int(input())
DP = [{} for i in range(N+1)]
M = int(input())
arr=[]
for i in range(M):
    arr.append(list(map(int, read().strip().split())))

arr.sort(key=lambda x:x[1])

def getBasicFactors(factor, amount):
    if DP[factor]=={}:
        return [[factor, amount]]
    else:
        RET=[]
        for k, v in DP[factor].items():
            RET.append([k, v*amount])
    return RET

for i in range(M):
    toAdded=getBasicFactors(arr[i][1], arr[i][2])
    for j in range(len(toAdded)):
        if DP[arr[i][0]].get(toAdded[j][0])==None:
            DP[arr[i][0]][toAdded[j][0]]=0
        DP[arr[i][0]][toAdded[j][0]] += toAdded[j][1]

toPrint = sorted(DP[N].items())
for i in range(len(toPrint)):
    print(toPrint[i][0], toPrint[i][1])