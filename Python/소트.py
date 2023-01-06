import sys
input = sys.stdin.readline

def find(start, end, target):
    for i in range(start, end):
        if nums[i] == target:
            return i

N = int(input())
nums = list(map(int,input().split()))
S = int(input())

for start in range(N - 1):
    end = min(start + S + 1, N)
    maxx = max(nums[start:end])

    index = find(start, end, maxx)
    dist = index - start
    if dist == 0: continue
    S -= dist

    #  start   index
    # 1 (2) 3 4 [5] 6 -> 1 [5] (2) 3 4 6
    nums = nums[:start] + [nums[index]] + [nums[start]] + nums[start+1:index] + nums[index+1:]
    
    if S == 0: break

print(*nums)