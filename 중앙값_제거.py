import sys      
from queue import PriorityQueue
import math

input = sys.stdin.readline  

if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    
    if(nums[0] == 0):
        print(0)
    else:    
        count = 0
        for i in range((N+1)//2):
            count += int(math.log2(nums[i]))  
                                
        print(count + 1)     