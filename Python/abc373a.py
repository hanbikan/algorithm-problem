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
map(int,input().split()
list(map(int,input().split())
'''

sys.setrecursionlimit(10**6)

cnt = 0
for i in range(12):
    s = input().rstrip()
    if len(s) == i + 1:
        cnt += 1
print(cnt)