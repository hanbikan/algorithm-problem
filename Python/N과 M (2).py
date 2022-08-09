import sys
import itertools
input = sys.stdin.readline

if __name__ == '__main__':
    N, M = map(int, input().split())

    nums = [i for i in range(1, N+1)]
    combinations = list(itertools.combinations(nums, M))

    for nums in combinations:
        for num in nums:
            print(num, end=" ")
        print()
