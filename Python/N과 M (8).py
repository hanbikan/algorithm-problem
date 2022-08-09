import sys
import itertools
input = sys.stdin.readline

if __name__ == '__main__':
    N, M = map(int, input().split())

    # sets
    sets = list(itertools.combinations_with_replacement(
        sorted(list(map(int, input().split()))), M))

    sets.sort()

    # 출력
    for set in sets:
        for n in set:
            print(n, end=" ")
        print()
