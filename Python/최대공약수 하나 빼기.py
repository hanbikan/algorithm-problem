from math import gcd
import sys
input = sys.stdin.readline

def gcd(x, y):
    if y != 0:
        return gcd(y, x % y)
    else:
        return x

N = int(input())
nums = list(map(int,input().split()))

l_to_r = []
r_to_l = [0] * N

l_to_r.append(nums[0])
for i in range(1, N):
    l_to_r.append(gcd(l_to_r[i - 1], nums[i]))

r_to_l[-1] = nums[-1]
for i in range(N - 2, -1, -1):
    r_to_l[i] = gcd(r_to_l[i + 1], nums[i])

#
result = 0
result_index = 0
for i in range(N):
    if i == 0:
        cur = r_to_l[i + 1]
    elif i == N - 1:
        cur = l_to_r[i - 1]
    else:
        cur = gcd(l_to_r[i - 1], r_to_l[i + 1])
    
    if cur > result:
        result = cur
        result_index = i

if nums[result_index] % result == 0:
    print(-1)
else:
    print(result, nums[result_index])