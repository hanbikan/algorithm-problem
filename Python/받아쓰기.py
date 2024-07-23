import sys
input = sys.stdin.readline

N, M = map(int, input().split())
word = str(input().rstrip())
answer = str(input().rstrip())

i_rep = set(['j','l'])

dp = [[i]+[0]*M for i in range(N + 1)]
dp[0] = [i for i in range(M + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        if word[i-1] == answer[j-1] or (word[i-1] == 'i' and answer[j-1] in i_rep) or (word[i-1] == 'v' and answer[j-1] == 'w'):
            dp[i][j] = dp[i-1][j-1]
print(dp[-1][-1])