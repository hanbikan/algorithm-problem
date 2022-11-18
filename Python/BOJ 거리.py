import sys
input = sys.stdin.readline

N = int(input())
strr = str(input().rstrip())

dictt = {'B': 0, 'O': 1, 'J': 2}

dp = [float('inf')]*N
dp[0] = 0

for i in range(N):
    for j in range(i+1, N):
        if (dictt[strr[i]] + 1) % 3 == dictt[strr[j]]:
            cost = (j - i)**2
            dp[j] = min(dp[j], dp[i] + cost)

print(dp[-1] if dp[-1] != float('inf') else -1)