# -*- coding: utf-8 -*-
import sys, math
input = sys.stdin.readline
                              
def get_gcd(left, right):    
  res = nums[left]
  for i in range(left+1, right):        
    res = math.gcd(res, nums[i])

    if res == 1:
      return 1

  return res

def f(left, right):
  if right - left == 1:
    return nums[left]                               
                     
  mid = (left + right)//2
  return max(
    f(left, mid) + get_gcd(mid, right),
    f(mid, right) + get_gcd(left, mid)
  )

if __name__ == '__main__':
  N = int(input())
  nums = list(map(int, input().split()))

  print(f(0, len(nums)))