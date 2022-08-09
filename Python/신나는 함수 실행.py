import sys
input = sys.stdin.readline
MAX = 101

def w(a, b, c):
    if dp[a][b][c] == -1:
        if a <= 0 or b <= 0 or c <= 0:
            dp[a][b][c] = 1
        elif a > 20 or b > 20 or c > 20:
            dp[a][b][c] = w(20, 20, 20)
        elif a < b and b < c:
            dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        else:
            dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + \
                w(a-1, b, c-1) - w(a-1, b-1, c-1)

    return dp[a][b][c]


if __name__ == '__main__':
    a, b, c = map(int, input().split())
    dp = [[[-1]*MAX for _ in range(MAX)] for _ in range(MAX)]
    while not (a == -1 and b == -1 and c == -1):
        print("w({0}, {1}, {2}) = {3}".format(a, b, c, w(a, b, c)))

        a, b, c = map(int, input().split())
