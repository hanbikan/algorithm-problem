import sys
input = sys.stdin.readline

def f(k):
    mul = 1
    while mul * 2 < k:
        mul *= 2

    count = 0
    while k >= 1:
        if k % mul != k:
            k %= mul
            count += 1
        mul //= 2

    return count % 2

k = int(input()) - 1
print(f(k))