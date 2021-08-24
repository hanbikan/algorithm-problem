import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())
    nums = [[0]*(m+1)] + [[0] + [int(c) for c in str(input().rstrip())]
                          for _ in range(n)]

    dp = [[0]*(m+1) for _ in range(n+1)]
    max_length = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if nums[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_length = max(max_length, dp[i][j])
            else:
                dp[i][j] = 0

    print(max_length**2)
