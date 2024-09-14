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

ab,ac,bc = map(str,input().split())
if ab == '<':
    if bc == '<':
        print("B")
    else:
        if ac == '<':
            print("C")
        else:
            print("A")
else:
    if ac == '<':
        print("A")
    else:
        if bc == '<':
            print("C")
        else:
            print("B")