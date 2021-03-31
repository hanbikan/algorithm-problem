import sys
input = sys.stdin.readline


def dfs(num, cnt):
    if num == B:
        global Min
        if Min == -1:
            Min = cnt
        else:
            Min = min(Min, cnt)
        return

    nextNum = num*2
    if nextNum <= B:
        dfs(nextNum, cnt+1)
    nextNum = int(str(num)+'1')
    if nextNum <= B:
        dfs(nextNum, cnt+1)


A, B = map(int, input().split())
Min = -1
dfs(A, 1)
print(Min)
