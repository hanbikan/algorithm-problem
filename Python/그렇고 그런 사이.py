import sys
input = sys.stdin.readline

N, K = map(int, input().split())
cur = [i for i in range(1, N+1)]
cur_k = K
result = []
for i in range(N):
    cur.sort(reverse=True)
    l = len(cur) - 1
    for c in cur:
        if l <= cur_k:
            cur_k -= l
            cur.remove(c)
            result.append(c)
            break
        l -= 1
print(*result)