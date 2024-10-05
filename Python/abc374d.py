import heapq
from bisect import bisect_left, bisect_right
from collections import deque
import collections
import itertools
from itertools import combinations
import sys, math
import random
input = sys.stdin.readline

'''
int(input())
map(int,input().split())
list(map(int,input().split()))
'''

sys.setrecursionlimit(10**6)

def calc(p1, p2):
    return math.sqrt(pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2))


N, S, T = map(int,input().split())
pos_pairs = []
for _ in range(N):
    A, B, C, D = list(map(int,input().split()))
    pos_pairs.append([(A,B), (C,D)])

def dfs(index, cur_pos, wasted):
    if index == N:
        global result
        result = min(result, wasted)
        return

    for i in range(2):
        next_wasted = wasted
        next_wasted += calc(cur_pos, cb[index][i]) / S
        next_wasted += calc(cb[index][i], cb[index][(i + 1) % 2]) / T
        dfs(index + 1, cb[index][(i + 1) % 2], next_wasted)

result = float('inf')
for cb in itertools.permutations(pos_pairs, N):
    dfs(0, (0, 0), 0.0)

print(result)