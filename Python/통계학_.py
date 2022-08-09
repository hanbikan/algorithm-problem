import sys
input = sys.stdin.readline

def get_mode(nums):
  counts = {}
  max_count = 0
  for num in nums:
    if(not counts.get(num)):
      counts[num] = 1
    else:
      counts[num] += 1
    
    max_count = max(max_count, counts[num])

  modes = []
  for num, count in counts.items():
    if(count == max_count):
      modes.append(num)

  if(len(modes) == 1):
    res = modes[0]
  else:       
    modes.sort()
    res = modes[1]
  return res

if __name__ == '__main__':
  N = int(input())
  nums = [int(input()) for _ in range(N)]

  nums.sort()
  print(round(sum(nums)/N))
  print(nums[N//2])
  print(get_mode(nums))
  print(max(nums) - min(nums))