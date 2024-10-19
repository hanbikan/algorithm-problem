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
map(int, input().split())
list(map(int, input().split()))
'''

sys.setrecursionlimit(10**6)

N, C = map(int, input().split())
T = list(map(int,input().split()))

count = 0
last = -float('inf')
for i in range(N):
    if T[i] - last >= C:
        count += 1
        last = T[i]
print(count)