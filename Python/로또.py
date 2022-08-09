import sys
input = sys.stdin.readline

def f(index):
    if len(stack) == 6: print(*stack)
    if index > n-1: return

    for i in range(index, n):
        stack.append(nums[i])
        f(i+1)
        stack.pop()


if __name__ == '__main__':
    while(True):
        nums = list(map(int,input().split()))
        n = nums[0]
        if n == 0: break
        nums = nums[1:]

        stack = []
        f(0)
        print()