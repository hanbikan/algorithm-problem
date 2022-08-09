import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, T = map(int, input().split())
    dp = [0]*(T+1)

    for i in range(N):
        k, s = map(int, input().split())

        for j in range(T, k-1, -1):
            dp[j] = max(dp[j], dp[j-k] + s)

    print(dp[-1])
