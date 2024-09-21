import heapq
from bisect import bisect_left, bisect_right
from collections import deque
import collections
import itertools
from itertools import combinations
import sys, math
import random
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

M = int(input())
cur_m = M
cur_n = 0
res = []
while cur_m > 0:
    i = 1
    j = 0
    while i <= cur_m:
        i *= 3
        j += 1
    cur_m -= i // 3
    res.append(j - 1)
    cur_n += 1

print(cur_n)
print(*res)