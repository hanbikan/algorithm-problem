N = int(input())
nums=list(map(int, input().split()))
dp = [nums[0]]
for i in range(1, N):
    dp.append(max(dp[i-1]+nums[i], nums[i]))
print(max(dp))