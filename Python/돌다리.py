import sys
input = sys.stdin.readline

def f():
    if (N == M):
        return 0

    dp = [float('inf')] * (100001)
    dp[N] = 0
    q = [N]

    while (len(q) > 0):
        nq = []
        while (len(q) > 0):
            cur = q.pop(0)
            nexts = [cur - 1, cur + 1, cur + A, cur - A, cur + B, cur - B, cur * A, cur * B]
            for nxt in nexts:
                if 0 <= nxt <= 100000:
                    if dp[cur] + 1 < dp[nxt]:
                        dp[nxt] = dp[cur] + 1
                        if nxt == M:
                            return dp[nxt]
                        nq.append(nxt)
        q = nq
    
    return -1

A, B, N, M = map(int, input().split())
print(f())