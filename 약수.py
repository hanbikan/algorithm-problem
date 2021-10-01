import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    print(min(nums)*max(nums))
