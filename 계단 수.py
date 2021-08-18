import sys
input = sys.stdin.readline


def getStairNumberCount(N):
    dp = [[] for _ in range(101)]
    dp[10] = [[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]]

    # return dp[N]


if __name__ == '__main__':
    N = int(input())
    print(getStairNumberCount(N))
