import sys
input = sys.stdin.readline

p1, p2, p3, index = map(int, input().split())

# 2^60 = 1.1529215e+18
nums = []
for i in range(61):
    a = p1 ** i
    for j in range(61):
        b = p2 ** j
        for k in range(61):
            c = p3 ** k
            nums.append(a * b * c)
nums.sort()
print(nums[index])