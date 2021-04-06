def findParent(x):
    if parent[x] == x:
        return x
    p = findParent(parent[x])
    parent[x] = p
    return parent[x]


def union(x, y):
    x = findParent(x)
    y = findParent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


G = int(input())
P = int(input())
airplanes = [int(input()) for _ in range(P)]

parent = {i: i for i in range(G+1)}

cntDocked = 0
for airplane in airplanes:
    x = findParent(airplane)
    if x == 0:
        break
    union(x, x-1)
    cntDocked += 1

print(cntDocked)
