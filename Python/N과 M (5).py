import sys
import itertools
input = sys.stdin.readline

if __name__ == '__main__':
    N, M = map(int, input().split())

    permutations = list(itertools.permutations(
        list(map(int, input().split())), M))
    permutations.sort()

    for nums in permutations:
        for num in nums:
            print(num, end=" ")
        print()
