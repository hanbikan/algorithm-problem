import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
DIV = 10007
NOT_DEFINED = -1


def get_combination(n, k):
    if k == 0 or k == n:
        return 1
    if dp[n][k] == NOT_DEFINED:
        dp[n][k] = (get_combination(n-1, k-1) + get_combination(n-1, k)) % DIV

    return dp[n][k]


if __name__ == '__main__':
    N, K = map(int, input().split())
    dp = [[NOT_DEFINED]*1001 for _ in range(1001)]
    dp[0][0] = 1
    print(get_combination(N, K))
