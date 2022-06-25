from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        to_print = "SYJKGW"

        nums = list(map(int, input().split()))
        length = nums[0]
        counts = defaultdict(int)

        for i in range(1, length+1):
            counts[nums[i]] += 1
            if counts[nums[i]] > length/2:
                to_print = nums[i]
                break
        
        print(to_print)