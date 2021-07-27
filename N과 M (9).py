import sys
import itertools
input = sys.stdin.readline

if __name__ == '__main__':
    N, M = map(int, input().split())
    nums = map(int, input().split())

    for cur in sorted(list(set(itertools.permutations(nums, M)))):
        print(*cur)
