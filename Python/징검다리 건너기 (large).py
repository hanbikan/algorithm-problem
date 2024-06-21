import sys, collections
input = sys.stdin.readline

def get_dist(a, b):
    return (b - a) * (1 + abs(nums[a] - nums[b]))

N = int(input())
nums = list(map(int, input().split()))

dp = [float('inf')]*N
dp[0] = 0
q = collections.deque([(0, 0)])
while q:
    dist, node = q.popleft()
    for next_node in range(node + 1, N):
        next_dist = max(dist, get_dist(node, next_node))

        if next_dist < dp[next_node]:
            dp[next_node] = next_dist
            q.append((next_dist, next_node))

print(dp[-1])