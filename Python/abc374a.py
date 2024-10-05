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

S = input().rstrip()
if len(S) < 3:
    print("No")
elif S[-3:] == "san":
    print("Yes")
else:
    print("No")