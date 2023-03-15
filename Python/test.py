from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
import sys
input = sys.stdin.readline

a = list("asd")
a[2] = 'c'
print(a)