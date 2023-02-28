import sys
input = sys.stdin.readline

def get_min_d():
    if M == 1:
        outer = [nums[i][0] for i in range(N)]
    else:
        outer = nums[0] + [nums[i][0] for i in range(1, N)] + [nums[i][-1] for i in range(1, N)]
    outer.sort()

    return outer[K - 1]

N, M, K = map(int,input().split())
nums = [list(map(int,input().split())) for _ in range(N)]
print(get_min_d())