from bisect import bisect_right
from itertools import combinations
import sys
input = sys.stdin.readline

# Input
N, M = map(int, input().split())
wacks = [0] + list(map(int, input().split()))

# Set steps
steps = set()
for cb in combinations(wacks, 2):
    steps.add(sum(cb))
steps = list(steps)
steps.sort()

# Solution: DP
dp = [float('inf')]*(N+1)
dp[0] = 0
for i in range(1, N+1):
    start_step_index = bisect_right(steps, i) - 1
    if start_step_index < 0: continue
    for j in range(start_step_index, -1, -1):
        dp[i] = min(dp[i], dp[i - steps[j]] + 1)

# Print the result
if dp[-1] == float('inf'):
    print(-1)
else:
    print(dp[-1])