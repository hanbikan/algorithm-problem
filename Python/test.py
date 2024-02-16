from bisect import bisect_left, bisect_right
from itertools import combinations
import sys
import random
input = sys.stdin.readline

# N = random.randrange(2, 4)
a = [2,5,1,4,3]
for i in range(5):
    for j in range(5 - 1 - i):
        if a[j] > a[j + 1]:
            tmp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = tmp
print(a)