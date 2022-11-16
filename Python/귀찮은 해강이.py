import sys
input = sys.stdin.readline

def find(x):
    if parents[x] == x:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

def union(x, y):
    px = find(x)
    py = find(y)

    if px < py:
        parents[py] = px
    else:
        parents[px] = py

N, M = map(int,input().split())
parents = [i for i in range(N+1)]
for _ in range(M):
    i, j = map(int,input().split())
    union(i, j)

res = 0
seq = list(map(int,input().split()))
for i in range(N-1):
    cur, nxt = seq[i], seq[i+1]
    if find(cur) != find(nxt):
        res += 1

print(res)