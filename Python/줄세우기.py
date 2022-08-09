import sys
read = sys.stdin.readline
N=int(read())
DP=[0 for i in range(N)]
maxDP=0
nums=[]
for i in range(N):
    nums.append(int(read()))
    tmp = 1
    for j in range(i):
        if nums[j]<nums[i] and tmp <= DP[j]:
            tmp = DP[j]+1
            if tmp>maxDP:
                maxDP=tmp
    DP[i]=tmp
print(N-maxDP)