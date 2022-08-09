import sys
read = sys.stdin.readline

def IsCalculatable(weights, marble):
    DP=[False for i in range(15001)]
    DP2=[]
    for i in range(len(weights)-1, -1, -1):
        toAppend=[]
        for j in range(len(DP2)):
            toAppend.append(weights[i]+DP2[j])
            if weights[i]-DP2[j]>=1:
                toAppend.append(weights[i]-DP2[j])
            elif DP2[j]-weights[i]>=1:
                toAppend.append(DP2[j]-weights[i])
        toAppend.append(weights[i])

        for j in range(len(toAppend)):
            if toAppend[j]==marble: return True
            if not DP[toAppend[j]]:
                DP[toAppend[j]]=True
                DP2.append(toAppend[j])

    return False

N = int(input())
weights = list(map(int, read().strip().split()))
M = int(input())
marbles = list(map(int, read().strip().split()))

for i in range(len(marbles)):
    if IsCalculatable(weights, marbles[i]):
        print("Y",end=' ')
    else: print("N",end=' ')