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

L, R = map(int, input().split())
if L == 1 and R == 0:
    print("Yes")
elif L == 0 and R == 1:
    print("No")
else:
    print("Invalid")