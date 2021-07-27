import sys
import itertools
input = sys.stdin.readline

if __name__ == '__main__':
    N, M = map(int, input().split())
    nums = sorted(set(input().split()), key=lambda x: int(x))

    for cur in itertools.combinations_with_replacement(nums, M):
        print(*cur)
