import sys
input = sys.stdin.readline

def solution():
    res = 1
    for i in range(2, N + 1):
        res = res * i
        while res % 10 == 0:
            res //= 10
        res %= 1000000 # Consider 15!
    while res % 10 == 0:
        res //= 10
    return res % 10

N = int(input())
print(solution())