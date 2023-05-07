from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
from queue import PriorityQueue
import sys
input = sys.stdin.readline

queue = PriorityQueue()
queue.put([1,2,3])
queue.put([0,6,3])
queue.put([2,3,1])
print(queue.get())