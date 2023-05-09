import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [
    [],
    set(["1"]),
    set(["1+1","2"]),
    set(["1+1+1","1+2","2+1","3"])
]
for i in range(4, n + 1):
    next_dp = set()
    for j in range(1, 3 + 1):
        for strr in dp[i - j]:
            next_dp.add("{0}+{1}".format(strr, j))
    dp.append(next_dp)
if k <= len(dp[n]):
    print(sorted(list(dp[n]))[k - 1])
else:
    print(-1)