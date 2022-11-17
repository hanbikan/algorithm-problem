import sys
input = sys.stdin.readline

VALUE, COUNT = 0, 1

def find(x):
    if parents[x][VALUE] == x:
        return parents[x]
    if parents[x][VALUE] != x:
        res = find(parents[x][VALUE])
        parents[x][VALUE] = res[VALUE]
        return res

def union(x, y):
    px_value, px_count = find(x)
    py_value, py_count = find(y)

    # py -> px
    if px_value < py_value:
        parents[py_value] = [px_value, 0]
        parents[px_value][COUNT] = px_count + py_count
    elif px_value > py_value:
        parents[px_value] = [py_value, 0]
        parents[py_value][COUNT] = px_count + py_count

parents = [[i,1] for i in range(10**6+1)]

N = int(input())
for _ in range(N):
    order = list(map(str,input().rstrip().split()))
    if order[0] == 'I':
        a, b = int(order[1]), int(order[2])
        union(a, b)
    else:
        c = int(order[1])
        print(find(c)[COUNT])