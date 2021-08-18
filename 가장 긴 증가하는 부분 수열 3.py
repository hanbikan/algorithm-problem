import sys
import bisect
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))

    stack = []
    for n in nums:
        index = bisect.bisect_left(stack, n)

        if index == len(stack):
            stack.append(n)
        else:
            stack[index] = n

    print(len(stack))
