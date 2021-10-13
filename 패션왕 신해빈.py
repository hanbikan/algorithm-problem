import sys
import itertools
input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())

        # Set items
        items = {}
        for _ in range(n):
            a, b = map(str, input().rstrip().split())
            if items.get(b):
                items[b] += 1
            else:
                items[b] = 1

        # Solution: Set & Print res
        res = 1
        for v in items.values():
            res *= v + 1
        print(res-1)
