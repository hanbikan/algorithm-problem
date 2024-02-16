import sys
input = sys.stdin.readline

def check_from(nums1, nums2, index):
    for i in range(N):
        if nums1[i] != nums2[(index + i) % N]:
            return False
    return True

def check(target):
    for i in range(N):
        if check_from(origin, target, i):
            return True
        if check_from(opposite_direction, target, i):
            return True
    return False

N = int(input())
origin = list(map(int, input().split()))

opposite_direction = []
for n in origin:
    opposite_direction.append((n + 1) % 4 + 1)
opposite_direction.reverse()

M = int(input())
result = []
for _ in range(M):
    cur = list(map(int, input().split()))
    if check(cur):
        result.append(cur)

# Print
print(len(result))
for nums in result:
    print(*nums)