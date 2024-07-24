import sys, collections
input = sys.stdin.readline

def find_index(target):
    l, r = 0, len(time_to_chars) - 1
    while l <= r:
        m = (l + r) // 2
        if time_to_chars[m][0] >= target:
            r = m - 1
        else:
            l = m + 1

    return l

N = int(input())
time_to_chars = collections.deque([[0, []]])
index = 1
for _ in range(N):
    order, a, time = input().rstrip().split(' ')
    time = int(time)
    if order == "type":
        time_to_chars.append([time, time_to_chars[-1][1].copy() + [a]])
    else:
        a = int(a)
        found = max(0, find_index(time - a) - 1)
        time_to_chars.append([time, time_to_chars[found][1].copy()])

to_print = time_to_chars[-1][1]
for c in to_print:
    print(c,end='')
'''
5
type a 1
type b 3
type c 5
undo 100 10000
type d 1001

5
type a 1
type b 3
type c 5
undo 100 6
type d 7

5
type a 1
type b 2
type c 3
undo 3 5
type d 7

7
type a 1
type b 2
type c 3
type d 4
type e 5
undo 3 7
type f 8
'''