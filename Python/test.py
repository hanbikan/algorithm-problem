import sys
import random
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
        print(nums)
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
        result = min(result, dfs(index, nums, cost + 7))
        nums[index] += 1
        nums[index + 1] += 1
        nums[index + 2] += 1
    
    if index + 1 < N and min(nums[index], nums[index + 1] >= 1):
        nums[index] -= 1
        nums[index + 1] -= 1
        result = min(result, dfs(index, nums, cost + 5))
        nums[index] += 1
        nums[index + 1] += 1
    
    if nums[index] >= 1:
        nums[index] -= 1
        result = min(result, dfs(index, nums, cost + 3))
        nums[index] += 1
    
    return result

#N = int(input())
#nums = list(map(int,input().split()))

for _ in range(10000):
    N = random.randrange(3, 10000)
    nums = []
    for i in range(N):
        nums.append(random.randrange(0, 10000))
    print(N)
    print(' '.join(map(str, nums)))
    
    #original, sol = dfs(0, nums, 0), solution()
    solution()
    #if (original != sol):
    #    print(original, sol)
    #    print("FAIL")
    #    break

'''
6 [4, 4, 3, 1, 2, 2]
6 [4, 4, 3, 1, 1, 4]

4
2 3 2 1

조건: 1 > 2


 @ @
 @@@
@@@@ 5 7 7 3

 @
@@@@

 @
 @@@
@@@@

 @
 @
@@@@

   @
 @ @
@@@@

 @ @
 @ @
@@@@
5 7 3 3 3
'''