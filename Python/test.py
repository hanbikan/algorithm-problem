from bisect import bisect_left
from collections import defaultdict, deque
import sys
input = sys.stdin.readline
 
a = [1,3,5]
print(bisect_left(a, 2))