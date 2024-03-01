from bisect import bisect_left, bisect_right
from itertools import combinations
import sys
import random
input = sys.stdin.readline

print(bisect_left([1,2,5,7], 0))
print(bisect_left([1,2,5,7], 1))
print(bisect_left([1,2,5,7], 3))
print(bisect_left([1,2,5,7], 9))
# N = random.randrange(2, 4)