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

A, B = map(int, input().split())

if A == B:
    print(1)
elif abs(A - B) % 2 == 0:
    print(3)
else:
    print(2)