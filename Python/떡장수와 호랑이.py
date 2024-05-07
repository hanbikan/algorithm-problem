import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(day, prev_cake):
    if day >= N:
        for cake in ate:
            print(cake)
        return True

    fail_count = 0
    for cake in matrix[day]:
        if not dp[day][cake] or cake == prev_cake:
            fail_count += 1
            continue

        ate.append(cake)
        if not dfs(day + 1, cake):
            fail_count += 1
            dp[day][cake] = False
        else:
            return True
        ate.pop()

    if fail_count == len(matrix[day]):
        return False
    else:
        return True

N = int(input())
matrix = [list(map(int, input().split()))[1:] for _ in range(N)]

dp = [[True]*10 for _ in range(N)]
ate = []

if not dfs(0, 0):
    print(-1)