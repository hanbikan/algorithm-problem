import sys
read = sys.stdin.readline

N=int(read())
nums=list(map(int, read().strip().split()))

DP=[[0]*21 for _ in range(N-1)]
DP[0][nums[0]]=1

for i in range(1, N-1):
    for j in range(21):
        prev = DP[i-1][j]
        if prev!=0:
            if j-nums[i]>=0: DP[i][j-nums[i]]+=prev
            if j+nums[i]<=20: DP[i][j+nums[i]]+=prev

print(DP[N-2][nums[-1]])