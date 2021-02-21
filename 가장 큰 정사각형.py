import sys
read = sys.stdin.readline
tmp=list(map(int, read().strip().split()))
n,m=tmp[0],tmp[1]
nums=[[-1 for i in range(m)] for j in range(n)]
for i in range(n):
    tmp=input()
    for j in range(m):
        nums[i][j]=int(tmp[j])

def getSquareLength(x, y):
    RET=0
    minLen = DP[x][y]
    for i in range(1, DP[x][y]):
        minLen = min(minLen, DP[x-i][y])
        RET+=1
        if i>=minLen: break
    return RET

maxLen = 0
DP=[[0 for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        if nums[i][j]==1:
            if j>=1: DP[i][j]=DP[i][j-1]+1
            elif j==0: DP[i][j]=1
        maxLen = max(maxLen, getSquareLength(i,j))

print(maxLen*maxLen)
