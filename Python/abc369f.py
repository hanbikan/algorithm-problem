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

H, W, N = map(int, input().split())
RC = [tuple(map(int, input().split())) for _ in range(N)]
RC.sort()

dp = [(float('inf'), float('inf'))]*N # column 기준 증가하는 수열
prev = {} # 경로
for r, c in RC:
    index = bisect_right(dp, (c, r))
    dp[index] = (c,r)
    prev[c,r] = dp[index-1] if index > 0 else (1,1)

while dp[-1][0] == float('inf'):
    dp.pop()
print(len(dp))

path = ['R'*(W - dp[-1][0]), 'D'*(H - dp[-1][1])]
cur_y, cur_x = dp[-1]
while (cur_x, cur_y) != (1, 1):
    prev_y, prev_x = prev[cur_y, cur_x]
    path.append('R' * (cur_y - prev_y) + 'D' * (cur_x - prev_x))
    cur_x, cur_y = prev_x, prev_y
print(''.join(path[::-1]))