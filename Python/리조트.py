import sys
input = sys.stdin.readline
COST1, COST3, COST5 = 10000, 25000, 37000


def dfs(date, coupon):
    # Base case
    if date > N:
        return 0

    # Skip the function if dp already exists
    if dp[date][coupon] != -1:
        return dp[date][coupon]

    # Recursive case
    if date in unavailable_dates:
        dp[date][coupon] = dfs(date+1, coupon)
        return dp[date][coupon]

    dp[date][coupon] = min(dfs(date+1, coupon) + COST1,
                           dfs(date+3, coupon+1) + COST3, dfs(date+5, coupon+2) + COST5)
    if coupon >= 3:
        dp[date][coupon] = min(dp[date][coupon], dfs(date+1, coupon-3))

    return dp[date][coupon]


if __name__ == '__main__':
    N, M = map(int, input().split())
    unavailable_dates = []
    if M > 0:
        unavailable_dates = list(map(int, input().split()))

    dp = [[-1]*(46) for _ in range(106)]
    print(dfs(1, 0))
