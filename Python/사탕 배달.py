from collections import deque
import sys
input = sys.stdin.readline

N, w = map(int,input().split())
three = deque()
five = deque()

for _ in range(N):
    t, s = map(int,input().split())
    if t == 3: three.append(s)
    else: five.append(s)

three = deque(sorted(three))
five = deque(sorted(five))

three_prefix_sum = deque([0])
for i in range(len(three)-1, -1, -1):
    three_prefix_sum.appendleft(three_prefix_sum[0] + three[i])
five_prefix_sum = deque([0])
for i in range(len(five)-1, -1, -1):
    five_prefix_sum.appendleft(five_prefix_sum[0] + five[i])

res = 0
five_count = min(w // 5, len(five))
for f in range(five_count + 1):
    t = min((w - 5*f) // 3, len(three))
    res = max(res, three_prefix_sum[len(three)-t] + five_prefix_sum[len(five)-f])

print(res)