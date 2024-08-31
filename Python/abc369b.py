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

N = int(input())
al = 0
ar = 0
result = 0
for _ in range(N):
    A, S = input().split()
    A = int(A)
    if S == 'L':
        if al != 0:
            result += abs(al - A)
        al = A
    else:
        if ar != 0:
            result += abs(ar - A)
        ar = A

print(result)