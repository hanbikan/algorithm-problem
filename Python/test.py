from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
import sys
input = sys.stdin.readline


def get_max_possible(n):
    cur = 1
    while cur * 4 <= n:
        cur *= 4
    return cur


for i in range(1, 100):
    print(i, get_max_possible(i))