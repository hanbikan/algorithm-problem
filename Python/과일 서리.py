import sys
input = sys.stdin.readline

def f(remain, index):
    if index == N - 1:
        return 1
    res = 0
    for i in range(1, remain):
        res += f(remain - i, index + 1)
    return res

N = int(input())
M = int(input())

print(f(M, 0))