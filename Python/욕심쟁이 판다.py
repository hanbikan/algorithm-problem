import sys
sys.setrecursionlimit(40000)
read = sys.stdin.readline

def getDP(nums, x, y):
    if DP[x][y]!=0: return DP[x][y]
    if x-1>=0 and nums[x][y]<nums[x-1][y]:
        DP[x][y]=max(getDP(nums, x-1, y)+1, DP[x][y])
    if y-1>=0 and nums[x][y]<nums[x][y-1]:
        DP[x][y]=max(getDP(nums, x, y-1)+1, DP[x][y])
    if x+1<=len(nums)-1 and nums[x][y]<nums[x+1][y]:
        DP[x][y]=max(getDP(nums, x+1, y)+1, DP[x][y])
    if y+1<=len(nums)-1 and nums[x][y]<nums[x][y+1]:
        DP[x][y]=max(getDP(nums, x, y+1)+1, DP[x][y])

    if DP[x][y]==0: DP[x][y]=1
    return DP[x][y]

N=int(input())
nums=[]
for i in range(N):
    nums.append(list(map(int,read().strip().split())))

DP=[[0 for i in range(N)] for j in range(N)]
RET=0
for i in range(N):
    for j in range(N):
        RET=max(RET, getDP(nums, i, j))

print(RET)