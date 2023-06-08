from collections import defaultdict
from math import sqrt
import sys
input = sys.stdin.readline

def factorization(n):
    result = set()

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n // i)
    
    return result

N = int(input())
nums = list(map(int,input().split()))
nums_set = set(nums)

scores = defaultdict(int)
for num in nums:
    # 12 = 2 * 2 * 3 -> 2, 3, 4, 6에 스코어 추가
    score_to_minus = 0
    factors = factorization(num)
    for factor in factors:
        if factor in nums_set:
            scores[factor] += 1
            score_to_minus += 1
    scores[num] -= score_to_minus

for num in nums:
    print(scores[num], end = (" " if num != nums[-1] else "\n"))