import sys, collections, bisect
input = sys.stdin.readline

N = int(input())
switches = list(map(int, input().split()))
bulbs = list(map(int, input().split()))

switch_to_index = {}
for i in range(N):
    bulb = bulbs[i]
    switch_to_index[bulb] = i

indexes = []
for i in range(N):
    switch = switches[i]
    indexes.append(switch_to_index[switch])

# LIS
stack = collections.deque()
indexes_of_stack = []
for i in range(N):
    cur = indexes[i]
    index_of_stack = bisect.bisect_left(stack, cur)
    indexes_of_stack.append(index_of_stack)
    if index_of_stack == len(stack):
        stack.append(cur)
    else:
        stack[index_of_stack] = cur

print(len(stack))
cur_target = len(stack) - 1
result = []
for i in range(N - 1, -1, -1):
    index_of_stack = indexes_of_stack[i]
    if index_of_stack == cur_target:
        result.append(switches[i])
        cur_target -= 1
result.sort()
print(*result)