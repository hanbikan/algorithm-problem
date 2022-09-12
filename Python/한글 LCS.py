import sys
input = sys.stdin.readline

str1 = str(input().rstrip())
str2 = input().rstrip()

dp = [[0]*(len(str1)+1) for _ in range(len(str2)+1)]
for i in range(1, len(str2)+1):
    for j in range(1, len(str1)+1):
        c1, c2 = str1[j-1], str2[i-1]
        if c1 == c2:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
maxx = max(max(dp[i]) for i in range(1, len(str2)+1))
print(maxx)