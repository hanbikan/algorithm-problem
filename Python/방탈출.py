import sys
input = sys.stdin.readline

N, M = map(int,input().split())
edges = [] # (weight, a, b)
for _ in range(M):
    a,b,w = map(int,input().split())
    edges.append((a,b,w))

T = list(map(int,input().split()))
for i in range(1,N+1):
    edges.append((0,i,T[i-1]))
edges.sort(key=lambda x:x[2])

parents = [i for i in range(N+1)]
def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x,y):
    px, py = find(x), find(y)
    if px < py:
        parents[py] = px
    else:
        parents[px] = py

result = 0
for a,b,w in edges:
    if find(a) != find(b):
        union(a,b)
        result += w
print(result)
'''
3 1
1 2 1000000
3 3 3

3 2
1 2 1
2 3 10000
100 100 100

3 2
1 2 1
2 3 1
100 100 100
'''