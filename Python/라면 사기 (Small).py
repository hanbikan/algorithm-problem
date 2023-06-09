import sys
input = sys.stdin.readline

costs = [3, 5, 7]

def buy(index, seq, count = 1):
    global cost

    for i in range(seq):
        nums[index + i] -= count
    cost += costs[seq - 1] * count

def solution():
    global cost

    cost = 0
    i = 0
    while i < N:
        if nums[i] == 0:
            i += 1
        elif i + 3 < N and nums[i + 1] > nums[i + 2] and nums[i + 3] >= 1:
            minn = min(nums[i], nums[i + 1], nums[i + 1] - nums[i + 2])
            buy(i, 2, 1 if minn <= 2 else minn - 2)
        elif i + 2 < N and min(nums[i], nums[i + 1], nums[i + 2]) >= 1:
            minn = min(nums[i], nums[i + 1], nums[i + 2])
            buy(i, 3, 1 if minn <= 2 else minn - 2)
        elif i + 1 < N and min(nums[i], nums[i + 1]) >= 1:
            minn = min(nums[i], nums[i + 1])
            buy(i, 2, 1 if minn <= 2 else minn - 2)
        else:
            buy(i, 1, 1 if nums[i] <= 2 else nums[i] - 2)

    return cost

N = int(input())
nums = list(map(int,input().split()))
print(solution())