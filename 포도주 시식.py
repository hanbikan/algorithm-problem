n = int(input())
wines = [0]
for i in range(n): wines.append(int(input()))
dp = [0, wines[1]]
if n>=2: dp.append(wines[1]+wines[2])

for i in range(3, n+1):
    dp.append(max(dp[i-1], dp[i-2]+wines[i], dp[i-3]+wines[i-1]+wines[i]))
print(dp[-1])