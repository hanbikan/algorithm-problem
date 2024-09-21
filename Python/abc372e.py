import heapq
from bisect import bisect_left, bisect_right
from collections import deque
import collections
import itertools
from itertools import combinations
import sys, math
import random

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)


def union_heapq(x, y):  # y를 x로 병합
    if x == y:
        return
    while parents[y][1]:
        p = heapq.heappop(parents[y][1])
        heapq.heappush(parents[x][1], p)

def find(x):
    if parents[x][0] == x:
        return parents[x]

    res = find(parents[x][0])
    parents[x][0] = res[0]
    union_heapq(res[0], parents[x][0])
    return res

def union(x, y):
    px, py = find(x)[0], find(y)[0]

    if px < py:  # py -> px 병합
        parents[py][0] = px
        union_heapq(px, py)
    else:
        parents[px][0] = py
        union_heapq(py, px)

N, Q = map(int, input().split())
parents = [[i, [-i]] for i in range(N+1)]

for _ in range(Q):
    o, u, v = map(int, input().split())
    if o == 1:
        union(u, v)
    else:
        res = find(u)
        if v > len(res[1]):
            print(-1)
        else:
            save = []
            for _ in range(v):
                save.append(heapq.heappop(res[1]))
            print(-save[-1])
            for s in save:
                heapq.heappush(res[1], s)