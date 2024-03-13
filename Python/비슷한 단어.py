from collections import defaultdict
from math import factorial
import sys
input = sys.stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]

simplified_dict = defaultdict(int)
for word in words:
    cur = []
    dictt = {}
    count = 0
    for c in word:
        if c not in dictt:
            dictt[c] = count
            count += 1
        cur.append(str(dictt[c]))
    simplified_dict[''.join(cur)] += 1

result = 0
for k, v in simplified_dict.items():
    if v <= 1: continue
    for i in range(v - 1, 0, -1):
        result += i
print(result)