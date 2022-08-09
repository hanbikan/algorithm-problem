import sys
input = sys.stdin.readline

MOD = 15746

if __name__ == '__main__':
    N = int(input())

    dp = [1, 1]
    pointer = 0
    for i in range(2, N+1):
        dp[pointer] = (dp[0] + dp[1]) % MOD
        pointer = (pointer + 1) % 2

    print(dp[(pointer+1) % 2])
