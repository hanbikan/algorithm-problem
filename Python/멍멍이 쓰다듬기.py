import sys
input = sys.stdin.readline

'''
0 1 2 3 3 4 4 5 5 5 6 6 6 7 7 7 7 8 8 8 8 
'''

def f():
    if diff < 3:
        return diff
    else:
        start_height = 3
        day = 3
        step = 2
        while True:
            if start_height <= diff < start_height + step:
                return day
            if start_height + step <= diff < start_height + step * 2:
                return day + 1
            start_height += 2 * step
            day += 2
            step += 1

X, Y = map(int, input().split())
diff = Y - X

print(f())