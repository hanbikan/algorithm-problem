import sys
input = sys.stdin.readline

def find(x):
    if parents[x] == x:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

def union(x, y):
    px, py = find(x), find(y)

    if px < py: parents[py] = px
    else: parents[px] = py

N, M = map(int,input().split())
types = [''] + list(map(str, input().rstrip().split()))
vertices = [list(map(int,input().split())) for _ in range(M)]

vertices.sort(key = lambda x:x[2])

res = 0
connected = 0
parents = [i for i in range(N+1)]
for a, b, dist in vertices:
    if types[a] == types[b]: continue

    if find(a) != find(b):
        union(a, b)
        res += dist
        connected += 1  
        if connected == N-1:
            break

if connected == N-1:
    print(res)
else:
    print(-1)