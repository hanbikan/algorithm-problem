from bisect import bisect_left, bisect_right
from collections import deque
from itertools import combinations
import sys
import random
input = sys.stdin.readline

#print(bisect_left([1,2,5,7], 0)) # 0
#print(bisect_left([1,2,5,7], 1)) # 0
#print(bisect_left([1,2,5,7], 3)) # 2
#print(bisect_left([1,2,5,7], 9)) # 4
#a = deque([[1,1]])
# N = random.randrange(2, 4)
s = "1234"
print(list(s))