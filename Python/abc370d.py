import heapq
from bisect import bisect_left, bisect_right
from collections import deque
import collections
import itertools
from itertools import combinations
import sys, math
import random
from sortedcontainers import SortedList

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

H, W, Q = map(int, input().split())

row = [SortedList(range(W)) for _ in range(H)]
col = [SortedList(range(H)) for _ in range(W)]

for t in range(Q):
    R, C = map(lambda x: int(x) - 1, input().split())

    # row 부수기
    index = bisect_left(row[R], C)
    if index < len(row[R]) and row[R][index] == C: # 벽 한 칸 부숨
        row[R].remove(C)
        col[C].remove(R)
        continue
    if index < len(row[R]): # 오른쪽 벽 부숨
        target = row[R][index]
        row[R].remove(target)
        col[target].remove(R)
    if index > 0: # 왼쪽 벽 부숨(index == 0이면 벽 하나만 부숴야 해서 if문 나눔)
        target = row[R][index - 1]
        row[R].remove(target)
        col[target].remove(R)

    # col 부수기
    index = bisect_left(col[C], R)
    if index < len(col[C]):
        target = col[C][index]
        col[C].remove(target)
        row[target].remove(C)
    if index > 0:
        target = col[C][index - 1]
        col[C].remove(target)
        row[target].remove(C)

print(sum(len(r) for r in row))