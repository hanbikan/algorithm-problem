from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
import sys
input = sys.stdin.readline
 
a = [1,3,5]
print(bisect_left(a, 0))
print(bisect_right(a, 0))
