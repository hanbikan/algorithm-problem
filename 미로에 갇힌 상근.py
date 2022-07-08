import sys
input = sys.stdin.readline

dx = [-2, -1, 1, 2, 1, -1]
dy = [0, 1, 1, 0, -1, -1]

def f(x, y, count):
    if count == 0:
        if x == 0 and y == 0:
            return 1
        else:
            return 0

    if dp[x][y][count] == -1:
        res = 0
        for k in range(6):
            nx, ny = x + dx[k], y + dy[k]
            if inrange(nx, ny):
                res += f(nx, ny, count - 1)
        dp[x][y][count] = res
    
    return dp[x][y][count]

def inrange(x, y):
    return -14 <= x <= 14 and -7 <= y <= 7

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        dp = [[[-1]*15 for _ in range(15)] for _ in range(29)]
        print(f(0, 0, n))