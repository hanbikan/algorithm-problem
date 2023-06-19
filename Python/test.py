import sys
import random
input = sys.stdin.readline

def solution():
    # TODO: Paste your solution function returning a minimum cost
    return 0

def dfs(index, nums, cost):
    if index >= N:
        return cost
    if nums[index] == 0:
        return dfs(index + 1, nums, cost)
    
    result = float('inf')
    if index + 2 < N and min(nums[index], nums[index + 1], nums[index + 2] >= 1):
        nums[index] -= 1
        nums[index + 1] -= 1
        nums[index + 2] -= 1
        result = min(result, dfs(index, nums, cost + costs[2]))
        nums[index] += 1
        nums[index + 1] += 1
        nums[index + 2] += 1
    
    if index + 1 < N and min(nums[index], nums[index + 1] >= 1):
        nums[index] -= 1
        nums[index + 1] -= 1
        result = min(result, dfs(index, nums, cost + costs[1]))
        nums[index] += 1
        nums[index + 1] += 1
    
    if nums[index] >= 1:
        nums[index] -= 1
        result = min(result, dfs(index, nums, cost + costs[0]))
        nums[index] += 1
    
    return result

for t in range(10000):
    N = random.randrange(1, 10)
    B = random.randrange(1, 10)
    C = random.randrange(1, 10)
    costs = [B, B + C, B + C * 2]
    nums = []
    for i in range(N):
        nums.append(random.randrange(0, 5))
    print("========case {0}========".format(t))
    print("N = {0}, B = {1}, C = {2}, costs = {3}".format(N, B, C, costs))
    print(' '.join(map(str, nums)))
    
    answer, my_solution = dfs(0, nums, 0), solution()
    if (answer != my_solution):
        print("Failed: answer = {0}, my solution = {1}".format(answer, my_solution))
        break
