from bisect import bisect_left, bisect_right
from itertools import combinations
import sys
import random
input = sys.stdin.readline

print(bisect_left([1,2,5,7], 0)) # 0
print(bisect_left([1,2,5,7], 1)) # 0
print(bisect_left([1,2,5,7], 3)) # 2
print(bisect_left([1,2,5,7], 9)) # 4
# N = random.randrange(2, 4)
lst = ['0','1','2']
print(''.join(lst))