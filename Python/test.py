
from collections import defaultdict, deque
from math import sqrt
from queue import PriorityQueue
import sys
input = sys.stdin.readline

def factorization(n):
    result = []

    cur_n = n
    for i in range(2, n + 1):
        while cur_n % i == 0:
            result.append(i)
            cur_n //= i

        if cur_n == 1: break
    
    return result

for i in range(1, 20):
    print(i, factorization(i))