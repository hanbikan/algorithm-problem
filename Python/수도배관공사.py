import sys
input = sys.stdin.readline

def compare_pairs(p1, p2):
    if p1[0] != p2[0]:
        return p1[0] > p2[0]
    else:
        return p1[1] > p2[1]

D, P = map(int,input().split())
lcs = [list(map(int,input().split())) for _ in range(P)]

prev_dp = [[0, float('inf')] for _ in range(D + 1)]
for i in range(1, P + 1):
    l, c = lcs[i - 1]
    dp = [[0, float('inf')]]
    for j in range(1, D + 1):
        if j >= l:
            new_dp_item = [prev_dp[j - l][0] + l, min(prev_dp[j - l][1], c)]
            if compare_pairs(new_dp_item, prev_dp[j]):
                dp.append(new_dp_item)
                continue
        dp.append(prev_dp[j])
    prev_dp = dp
print(dp[-1][1])